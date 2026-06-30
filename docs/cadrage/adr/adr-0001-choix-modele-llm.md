# ADR-0001 — Choix du modèle LLM pour la génération de quiz

| | |
|---|---|
| **Statut** | 🟡 Proposé *(à acter après exécution du [benchmark J2](../../perturbations/j2-technique.md))* |
| **Date** | 30/06/2026 |
| **Décideurs** | Équipe 6 (Kahil MOKHTARI, Amine HADDANE, Souleymane FALL, Nikola MILOSAVLJEVIC, Dina CHAOUKI, Rayan ZEBAZE SAO, Hugo RAGUIN) |
| **Story liée** | US-X.3 (tracer le choix LLM) · SPK-2 · contrainte US-W.3 (cloud = ADR obligatoire) |

---

## 1. Contexte

La génération de 10 QCM prend **~45 s** avec `llama3.1:8b` (Ollama, local) — jugé inacceptable par un beta-testeur (perturbation J2). Le sponsor exige **≤ 15 s** d'ici ce soir. Contrainte produit non négociable : **souveraineté des données (RGPD), 100 % local par défaut**. Il faut donc accélérer **sans** envoyer les cours des utilisateurs hors UE.

## 2. Options envisagées

| Option | Latence visée | Qualité | RGPD | Coût / effort |
|---|:--:|:--:|---|---|
| **A. Statu quo** `llama3.1:8b` (local) | ~45 s ❌ | élevée | ✅ local | nul — mais ne tient pas le SLA |
| **B. Modèle local plus léger** `phi3:mini` / `mistral:7b` (Ollama) | _à mesurer_ | bonne ? | ✅ local | faible (changer `OLLAMA_MODEL`) |
| **C. Cloud européen** Mistral AI `mistral-small` | rapide | élevée | 🟡 UE (hors local) | faible (clé API) |
| **D. Cloud US** Groq `llama-3.3-70b` | très rapide | élevée | ❌ hors UE | faible mais **conflit RGPD** |

> Chiffres médiane/p95 et qualité /5 : voir le [tableau de benchmark J2](../../perturbations/j2-technique.md#3-options-envisagées--tableau-de-benchmark-ca-j2-1).

## 3. Décision

> **Décision proposée (à confirmer par les chiffres du benchmark) :**
>
> 1. **Privilégier l'option B** — basculer sur le **modèle local le plus léger qui tient ≤ 15 s à qualité ≥ 4/5** (candidat principal : `phi3:mini`). La souveraineté est préservée.
> 2. **Repli option C (Mistral, cloud UE)** *uniquement* si **aucun** modèle local ne tient le SLA — fournisseur **européen** donc compatible RGPD, activable par configuration.
> 3. **Option D (Groq/US) exclue par défaut** (données hors UE) — réservée à une démo non-RGPD explicitement isolée.

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
- Un modèle plus léger peut **baisser la qualité** → surveiller la note /5 et le taux d'hallucination (US-F3.5, RAG).
- Le **prompt** peut nécessiter un ajustement par modèle.
- Si repli option C : dépendance à un tiers UE → mentionner dans les pages RGPD (US-G.1).

---

*ADR-0001 — équipe 6 · format Architecture Decision Record (1 page). À passer en statut « Accepté » une fois le benchmark exécuté et la cible ≤ 15 s vérifiée.*
