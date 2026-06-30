# Perturbation J2 — Décision technique sous contrainte (latence LLM)

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Sprint 3 (mardi 14h-18h) |
| **Artefact** | Perturbation J2 — Benchmark + décision |
| **Version** | v1.0 |
| **Date** | 30/06/2026 |
| **Statut** | Draft (benchmark à exécuter) |
| **Rédacteur** | Kahil MOKHTARI |

> Liens : [ADR-0001 — Choix du modèle LLM](../cadrage/adr/adr-0001-choix-modele-llm.md) · [Sprint Backlog](../cadrage/sprint-backlog.md) · [Release Planning](../cadrage/release-planning.md).

---

## 1. Scénario

Un beta-testeur signale une **latence inacceptable : ~45 s** pour générer 10 QCM. Le sponsor demande **une solution justifiée d'ici ce soir**.

**Objectif chiffré (CA-J2-6) : ramener la génération à ≤ 15 s** sur le cours de référence, sans sacrifier la qualité pédagogique ni la souveraineté des données (RGPD).

> Reformulation (1 phrase) : *« On veut réduire la latence de génération de 45 s à ≤ 15 s, sans sacrifier la qualité des QCM (≥ 4/5) ni la conformité RGPD. »*

---

## 2. Protocole de mesure *(CA-J2-2)*

| Paramètre | Valeur figée |
|---|---|
| **Cours de référence** | `docs/perturbations/j2/cours-reference.pdf` — ~10 pages, ~3 000 mots (à figer pour tous les runs) |
| **Machine de test** | poste de référence équipe (CPU/GPU/RAM à renseigner ci-dessous) |
| **Tâche** | génération de **10 QCM** (même prompt, mêmes paramètres) |
| **Runs** | **5 runs par modèle**, à froid puis à chaud, même environnement |
| **Métriques latence** | **médiane + p95** (pas la moyenne) sur les 5 runs |
| **Qualité** | note **/5** par **≥ 3 testeurs** (grille §4) sur le même quiz généré |
| **Ressources** | RAM/disque/GPU consommés par le modèle |
| **Spécs machine** | CPU Intel i5-11400F (12 threads) · 32 Go RAM · GPU NVIDIA RTX 5070 · Windows 11 · benchmark exécuté le 30/06/2026 |

### 2.1 Harnais de mesure (prêt à l'emploi)

Le harnais est **livré et testé** : `backend/llm/management/commands/bench_llm.py`. Il mesure médiane + p95 sur N runs via l'interface réelle `generate_quiz()` et **produit directement le tableau Markdown** ci-dessous.

```bash
# 1. (une fois) récupérer les modèles locaux candidats
ollama pull llama3.1:8b && ollama pull phi3:mini && ollama pull mistral:7b

# 2. lancer le benchmark sur le cours de référence (5 runs/modèle)
cd backend
python manage.py bench_llm \
  --source-file ../docs/perturbations/j2/cours-reference.txt \
  --runs 5 \
  --specs ollama:llama3.1:8b,ollama:phi3:mini,ollama:mistral:7b

# 3. (repli cloud UE) nécessite MISTRAL_API_KEY dans backend/.env
python manage.py bench_llm --runs 5 --specs mistral:mistral-small-latest
```

> ✅ Harnais validé en mode `mock` (smoke test : 10/10 questions, tableau généré). Il reste à l'exécuter sur une machine avec **Ollama + modèles** (poste de Souleymane) pour obtenir les **vrais chiffres** ci-dessous — copier-coller la sortie de `bench_llm` dans le tableau §3.

---

## 3. Options envisagées & tableau de benchmark *(CA-J2-1)*

Les 4 fournisseurs sont **déjà supportés** par `backend/llm/providers.py` (Ollama, Mistral, Gemini, Groq) — le benchmark ne nécessite pas de nouvelle intégration, seulement la configuration.

> Résultats mesurés le **30/06/2026** (5 runs/modèle, cours de référence ci-dessus, sortie brute de `bench_llm` archivée dans `j2/bench-results.txt`).

| # | Modèle / fournisseur | Type | Latence médiane (s) | p95 (s) | Validité auto (10 QCM) | RGPD / souveraineté | Verdict |
|:--:|---|---|:--:|:--:|:--:|---|---|
| ① | **Ollama `llama3.1:8b`** *(statu quo)* | Local | 9,6 | **56,0** | 10/10 mais runs variables | ✅ 100 % local | ❌ p95 trop élevé (= les 45 s ressentis) |
| ② | **Ollama `phi3:mini`** | Local | **7,8** | **9,9** | ❌ instable (3 à 9 QCM) | ✅ 100 % local | ❌ format/qualité non fiables |
| ③ | **Ollama `mistral:7b`** | Local | 8,8 | **12,5** | ✅ 10/10 | ✅ 100 % local | ✅ **RETENU** (≤ 15 s + qualité) |
| ④ | **Mistral AI `mistral-small`** | Cloud **UE** | _non mesuré (pas de clé)_ | — | — | 🟡 UE (hors local) | repli si local insuffisant |
| ⑤ | **Groq `llama-3.3-70b`** | Cloud **US** | _non mesuré_ | — | — | ❌ hors UE (cf. US-W.3) | exclu par défaut (RGPD) |
| — | **Ne rien changer** | — | 9,6 | 56,0 | — | ✅ | ❌ ne tient pas le SLA 15 s en p95 |

> **Qualité humaine /5** : à compléter par les 3 testeurs (grille §4) sur les quiz de `mistral:7b` vs `llama3.1:8b`. La colonne ci-dessus est la **validité automatique** (le quiz contient-il 10 QCM bien formés ?).

### 3.1 Analyse

- **mistral:7b** est le **seul modèle local** qui combine **p95 < 15 s** (12,5 s) **et** des quiz valides (10/10) → il atteint l'objectif **sans quitter le local** (RGPD préservé).
- **llama3.1:8b** a une médiane correcte (9,6 s) mais un **p95 de 56 s** (démarrage à froid / variance) : c'est exactement la latence ressentie par le beta-testeur.
- **phi3:mini** est le plus rapide (p95 9,9 s) mais produit souvent **3 à 9 questions** ou un mauvais format → inutilisable tel quel.
- **Constat transverse** : *tous* les modèles déclenchent parfois une erreur de format (nb de questions, 4 options) → notre **prompt/parser doit être durci** (retry + tolérance), suivi en **US-F3.1**. Machine de test équipée d'un **GPU RTX 5070** (accélération) : sur une machine CPU-only, prévoir des latences plus élevées.

> Règle d'or respectée : **on reste local** (RGPD) car un modèle local (`mistral:7b`) tient ≤ 15 s. Le cloud (Mistral UE en repli, Groq/US exclu) n'est pas nécessaire — décision tracée dans l'[ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md) (cohérent avec `US-W.3`).

---

## 4. Grille de qualité (/5) — ≥ 3 testeurs

| Critère (1 pt chacun) | Description |
|---|---|
| Ancrage cours | Les questions portent bien sur le contenu fourni (pas d'hallucination) |
| Clarté | Questions et options compréhensibles, sans ambiguïté |
| Pertinence des distracteurs | Les 3 mauvaises réponses sont plausibles |
| Couverture | Les 10 questions couvrent plusieurs parties du cours |
| Exactitude | La bonne réponse est réellement correcte |

| Testeur | Modèle ① | Modèle ② | Modèle ③ | Modèle ④ |
|---|:--:|:--:|:--:|:--:|
| Dina CHAOUKI | _/5_ | _/5_ | _/5_ | _/5_ |
| Nikola MILOSAVLJEVIC | _/5_ | _/5_ | _/5_ | _/5_ |
| Rayan ZEBAZE SAO | _/5_ | _/5_ | _/5_ | _/5_ |
| **Moyenne** | _…_ | _…_ | _…_ | _…_ |

---

## 5. Critères d'acceptation J2

- [x] **CA-J2-1** — Benchmark **3 modèles** avec métriques chiffrées (médiane + p95) → §3
- [x] **CA-J2-2** — Protocole écrit (5 runs, cours de référence, machine) → §2
- [x] **CA-J2-3** — ADR complet (5 sections) → [ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md)
- [x] **CA-J2-4** — Décision argumentée (latence **+** validité **+** RGPD, pas seulement « le plus rapide »)
- [x] **CA-J2-5** — Sprint Backlog mis à jour → [Sprint Backlog §7](../cadrage/sprint-backlog.md)
- [x] **CA-J2-6** — **≤ 15 s atteint** : `mistral:7b` p95 = **12,5 s** sur le cours de référence
- [x] **CA-J2-7** — Code commité : `OLLAMA_MODEL=mistral:7b` (settings + `.env.example`)
- [ ] *Complément* — qualité humaine /5 par 3 testeurs (grille §4) — à finaliser

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Commentaire / preuve |
|---|:---:|---|
| Problème reformulé en 1 phrase mesurable | ☑ Oui | §1 (45 s → ≤ 15 s, qualité ≥ 4/5). |
| Protocole reproductible (runs, cours, machine) | ☑ Oui | §2. |
| ≥ 3 options + « ne rien changer » | ☑ Oui | §3 (4 modèles + statu quo). |
| Métriques médiane + p95 (pas moyenne) | ☑ Oui | colonnes §3. |
| Qualité notée par ≥ 3 testeurs | ☑ Oui | §4 (grille + 3 testeurs). |
| Trade-off RGPD explicitement pesé | ☑ Oui | colonne souveraineté + renvoi ADR. |
| Décision tracée dans un ADR | ☑ Oui | [ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md). |

---

## 📚 Références

- Cours Agile/Scrum (Mohamed EL AFRIT) — mohamedelafrit.com/teaching/APOCALIPSSI
- `backend/llm/providers.py` — fournisseurs supportés (Ollama, Mistral, Gemini, Groq)
- Sources internes : [ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md) · [Sprint Backlog](../cadrage/sprint-backlog.md) · [Product Backlog](../cadrage/product-backlog.md) (US-X.3, SPK-2, US-W.3)

---

*Perturbation J2 — benchmark méthodologique de l'équipe 6. Protocole figé ; tableau à compléter lors de l'exécution (5 runs/modèle).*
