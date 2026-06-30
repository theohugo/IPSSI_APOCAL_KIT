# ADR-0001 — Choix du modèle LLM pour la génération de quiz

| | |
|---|---|
| **Statut** | ✅ **Accepté** *(benchmark J2 exécuté le 30/06/2026 — [résultats](../../perturbations/j2-technique.md#3-options-envisagées--tableau-de-benchmark-ca-j2-1))* |
| **Date** | 30/06/2026 |
| **Décideurs** | Équipe 6 (Kahil MOKHTARI, Amine HADDANE, Souleymane FALL, Nikola MILOSAVLJEVIC, Dina CHAOUKI, Rayan ZEBAZE SAO, Hugo RAGUIN) |
| **Story liée** | US-X.3 (tracer le choix LLM) · SPK-2 · contrainte US-W.3 (cloud = ADR obligatoire) |

---

## 1. Contexte

La génération de 10 QCM prend **~45 s** avec `llama3.1:8b` (Ollama, local) — jugé inacceptable par un beta-testeur (perturbation J2). Le sponsor exige **≤ 15 s** d'ici ce soir. Contrainte produit non négociable : **souveraineté des données (RGPD), 100 % local par défaut**. Il faut donc accélérer **sans** envoyer les cours des utilisateurs hors UE.

## 2. Options envisagées

| Option | Latence médiane / p95 | Validité (10 QCM) | RGPD | Verdict |
|---|:--:|:--:|---|---|
| **A. Statu quo** `llama3.1:8b` (local) | 9,6 s / **56,0 s** | 10/10 variable | ✅ local | ❌ p95 hors SLA |
| **B1. Local léger** `phi3:mini` (Ollama) | 7,8 s / 9,9 s | ❌ instable (3-9 QCM) | ✅ local | ❌ qualité non fiable |
| **B2. Local équilibré** `mistral:7b` (Ollama) | 8,8 s / **12,5 s** | ✅ 10/10 | ✅ local | ✅ **retenu** |
| **C. Cloud UE** Mistral AI `mistral-small` | non mesuré | — | 🟡 UE | repli si local insuffisant |
| **D. Cloud US** Groq `llama-3.3-70b` | non mesuré | — | ❌ hors UE | exclu (RGPD, US-W.3) |

> Mesures : 5 runs/modèle, cours de référence, machine i5-11400F + RTX 5070. Détail : [benchmark J2](../../perturbations/j2-technique.md#3-options-envisagées--tableau-de-benchmark-ca-j2-1).

## 3. Décision

> **Décision (actée sur la base du benchmark) :**
>
> 1. **Adopter l'option B2 — `mistral:7b` en local (Ollama)** comme modèle par défaut : **p95 12,5 s (< 15 s)** et **10 QCM valides**, **souveraineté préservée**. Appliqué via `OLLAMA_MODEL=mistral:7b` (settings + `.env.example`).
> 2. **`phi3:mini` écarté** malgré sa rapidité (p95 9,9 s) : qualité/format **non fiables** (3 à 9 questions).
> 3. **`llama3.1:8b` écarté** : p95 56 s (cause de la latence ressentie).
> 4. **Repli option C (Mistral cloud UE)** si un poste **sans GPU** ne tient pas le SLA en local. **Option D (Groq/US) exclue** (RGPD, US-W.3).
> 5. **Durcir le prompt/parser** (retry + tolérance) : tous les modèles ont parfois dévié du format → action **US-F3.1**.

## 4. Justification *(au-delà de « le plus rapide » — CA-J2-4)*

- **Souveraineté d'abord** : notre différenciateur produit et notre engagement RGPD imposent le local tant qu'il est viable ; on ne sacrifie pas la conformité pour quelques secondes.
- **Réversibilité** : `backend/llm/providers.py` permet de changer de fournisseur par **configuration** (feature-flag), sans réécriture — décision peu risquée et réversible.
- **Qualité maîtrisée** : le seuil ≥ 4/5 (3 testeurs) garantit qu'on n'échange pas la latence contre des QCM médiocres.
- **Coût** : option B = coût nul (modèle local déjà disponible) ; option C = coût maîtrisé (free tier Mistral).

## 5. Conséquences

**Positives (+)**
- Latence ramenée à ≤ 15 s, SLA beta-testeur respecté.
- RGPD/souveraineté préservés (option B) ; repli UE documenté (option C).
- Choix tracé et réversible (config).

**À surveiller (−)**
- **Robustesse du format** : tous les modèles ont parfois renvoyé un nombre de questions ≠ 10 → durcir le prompt/parser avec retry (**US-F3.1**).
- **Dépendance GPU** : les mesures sont sur une machine avec RTX 5070 ; sur un poste **CPU-only**, les latences seront plus élevées → réévaluer (repli option C possible).
- Surveiller la qualité /5 et le taux d'hallucination de `mistral:7b` (US-F3.5, RAG).
- Si repli option C : dépendance à un tiers UE → mentionner dans les pages RGPD (US-G.1).

---

*ADR-0001 — équipe 6 · format Architecture Decision Record (1 page) · statut **Accepté** le 30/06/2026 après benchmark (cible ≤ 15 s vérifiée avec `mistral:7b`).*
