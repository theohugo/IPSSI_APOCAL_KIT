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
| **Spécs machine** | _CPU : … · RAM : … · GPU : … · OS : …_ (à compléter) |

> Implémentation : harnais de mesure autour de l'appel de génération (`backend/llm/…`), 5 itérations chronométrées, export du tableau ci-dessous.

---

## 3. Options envisagées & tableau de benchmark *(CA-J2-1)*

Les 4 fournisseurs sont **déjà supportés** par `backend/llm/providers.py` (Ollama, Mistral, Gemini, Groq) — le benchmark ne nécessite pas de nouvelle intégration, seulement la configuration.

| # | Modèle / fournisseur | Type | Latence médiane (s) | p95 (s) | Qualité /5 | RAM | RGPD / souveraineté | Verdict |
|:--:|---|---|:--:|:--:|:--:|:--:|---|---|
| ① | **Ollama `llama3.1:8b`** *(statu quo)* | Local | _~45_ | _…_ | _…_ | _…_ | ✅ 100 % local | référence |
| ② | **Ollama `phi3:mini`** | Local | _…_ | _…_ | _…_ | _…_ | ✅ 100 % local | _à mesurer_ |
| ③ | **Ollama `mistral:7b`** | Local | _…_ | _…_ | _…_ | _…_ | ✅ 100 % local | _à mesurer_ |
| ④ | **Mistral AI `mistral-small`** | Cloud **UE** | _…_ | _…_ | _…_ | n/a | 🟡 UE (hors local) | _repli_ |
| ⑤ | **Groq `llama-3.3-70b`** | Cloud **US** | _…_ | _…_ | _…_ | n/a | ❌ hors UE (cf. US-W.3) | _exclu par défaut_ |
| — | **Ne rien changer** | — | ~45 | — | — | — | ✅ | ❌ ne tient pas le SLA 15 s |

> Règle d'or : **rester local** (RGPD) si un modèle local tient ≤ 15 s à qualité ≥ 4/5. Tout passage cloud doit être tranché par l'[ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md) (cohérent avec `US-W.3` du backlog).

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

- [ ] **CA-J2-1** — Benchmark ≥ 3 modèles avec métriques chiffrées
- [ ] **CA-J2-2** — Protocole écrit (runs, cours, machine) → §2
- [ ] **CA-J2-3** — ADR complet (≥ 4 sections) → [ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md)
- [ ] **CA-J2-4** — Décision argumentée au-delà du « plus rapide »
- [ ] **CA-J2-5** — Sprint Backlog visiblement mis à jour → [Sprint Backlog §7](../cadrage/sprint-backlog.md)
- [ ] **CA-J2-6** — **Temps final ≤ 15 s** sur le cours de référence
- [ ] **CA-J2-7** — Code commité (config modèle) ou justification claire

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
