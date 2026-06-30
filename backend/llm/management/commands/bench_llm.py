"""
Harnais de benchmark LLM — perturbation J2 (latence de génération de quiz).

Mesure, pour chaque modèle, la latence de `generate_quiz` sur un cours de
référence : médiane + p95 sur N runs (pas la moyenne), nombre de questions
valides, et type (local/cloud, RGPD). Produit un tableau Markdown prêt à
coller dans docs/perturbations/j2-technique.md.

Exemples
--------
# Cours de référence + 5 runs sur les 4 candidats J2 (Ollama local) :
python manage.py bench_llm --source-file ../docs/perturbations/j2/cours-reference.txt \
    --runs 5 --specs ollama:llama3.1:8b,ollama:phi3:mini,ollama:mistral:7b

# Ajouter le repli cloud européen (nécessite MISTRAL_API_KEY dans le .env) :
python manage.py bench_llm --runs 5 --specs mistral:mistral-small-latest

# Smoke test sans modèle (valide le harnais) :
python manage.py bench_llm --specs mock: --runs 3

[Note] Un « spec » = "<backend>:<model>". Le modèle peut contenir des « : »
(ex. mistral:7b) : seul le PREMIER « : » sépare backend et modèle.
"""

import statistics
import time

from django.conf import settings
from django.core.management.base import BaseCommand

from llm.providers import PROVIDERS
from llm.services.factory import _BACKENDS

# Candidats par défaut de la perturbation J2 (ordre = statu quo puis options).
DEFAULT_SPECS = "ollama:llama3.1:8b,ollama:phi3:mini,ollama:mistral:7b,mistral:mistral-small-latest"

# Cours de référence minimal embarqué (repli si --source-file absent).
# Pour un benchmark VALABLE, utilisez le vrai cours via --source-file.
SAMPLE = (
    "Le modèle OSI (Open Systems Interconnection) découpe les communications "
    "réseau en sept couches : physique, liaison de données, réseau, transport, "
    "session, présentation et application. La couche réseau (couche 3) gère "
    "l'adressage logique (IP) et le routage des paquets entre réseaux distincts. "
    "Le protocole OSPF (Open Shortest Path First) est un protocole de routage à "
    "état de liens qui calcule le plus court chemin avec l'algorithme de Dijkstra. "
    "La couche transport (couche 4) assure la fiabilité avec TCP (orienté "
    "connexion, contrôle de flux et de congestion) ou la rapidité avec UDP. "
) * 6


def parse_spec(spec: str) -> tuple[str, str]:
    backend, _, model = spec.partition(":")
    return backend.strip(), model.strip()


class Command(BaseCommand):
    help = "Benchmark de latence des modèles LLM (perturbation J2)."

    def add_arguments(self, parser):
        parser.add_argument("--specs", default=DEFAULT_SPECS,
                            help="Liste backend:model séparés par des virgules.")
        parser.add_argument("--runs", type=int, default=5,
                            help="Nombre de runs par modèle (>= 5 recommandé).")
        parser.add_argument("--source-file", default="",
                            help="Fichier texte du cours de référence (sinon échantillon embarqué).")
        parser.add_argument("--title", default="Cours de référence J2")

    def handle(self, *args, **opts):
        source = SAMPLE
        if opts["source_file"]:
            with open(opts["source_file"], encoding="utf-8") as fh:
                source = fh.read()
        runs = opts["runs"]
        title = opts["title"]
        self.stdout.write(self.style.NOTICE(
            f"Cours: {len(source)} caractères · {runs} runs/modèle\n"))

        rows = []
        for spec in [s for s in opts["specs"].split(",") if s.strip()]:
            backend, model = parse_spec(spec)
            prov = PROVIDERS.get(backend)
            label = (prov.label if prov else backend) + (f" `{model}`" if model else "")
            rgpd = "✅ local" if (prov and not prov.cloud) else "❌/🟡 cloud"
            client = self._make_client(backend, model)
            if client is None:
                rows.append((label, rgpd, "—", "—", "—", "client indisponible (clé manquante ?)"))
                continue
            lat, nq, err = [], None, ""
            for i in range(runs):
                t0 = time.perf_counter()
                try:
                    qs = client.generate_quiz(source_text=source, title=title)
                    lat.append(time.perf_counter() - t0)
                    nq = len(qs)
                except Exception as e:  # noqa: BLE001 - on veut tout capturer
                    dt = time.perf_counter() - t0
                    msg = str(e).lower()
                    err = f"{type(e).__name__}: {e}"[:80]
                    if "injoignable" in msg or "connection" in msg or "timeout" in msg:
                        break  # échec infra : latence non significative, on arrête
                    # Le modèle a RÉPONDU mais sortie invalide (ex. 9 Q) :
                    # la latence d'inférence est réelle, on la conserve.
                    lat.append(dt)
            if lat:
                med = statistics.median(lat)
                p95 = sorted(lat)[max(0, round(0.95 * len(lat)) - 1)]
                qval = f"{nq}/10" if nq is not None else "invalide"
                rows.append((label, rgpd, f"{med:.1f}", f"{p95:.1f}", qval, err or "ok"))
            else:
                rows.append((label, rgpd, "—", "—", "—", err or "échec"))

        self._print_table(rows)

    def _make_client(self, backend, model):
        cls = _BACKENDS.get(backend)
        if cls is None:
            return None
        try:
            if backend == "mock":
                return cls()
            if backend == "ollama":
                return cls(model=model or None)
            prov = PROVIDERS.get(backend)
            key = getattr(settings, prov.settings_key_attr, "") if (prov and prov.settings_key_attr) else ""
            if prov and prov.needs_key and not key:
                return None  # pas de clé → on saute proprement
            return cls(api_key=key, model=model or None)
        except Exception:  # noqa: BLE001
            return None

    def _print_table(self, rows):
        self.stdout.write("\n| Modèle | RGPD | Latence médiane (s) | p95 (s) | Q valides | Note |")
        self.stdout.write("|---|---|:--:|:--:|:--:|---|")
        for label, rgpd, med, p95, nq, note in rows:
            self.stdout.write(f"| {label} | {rgpd} | {med} | {p95} | {nq} | {note} |")
        self.stdout.write("")
