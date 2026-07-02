# ADR-0003 — Migration vers une architecture scalable

| | |
|---|---|
| **Statut** | ✅ **Accepté** *(décision actée le 02/07/2026 — réponse à la perturbation J4 « passage à l'échelle »)* |
| **Date** | 02/07/2026 |
| **Décideurs** | Équipe 6 (Kahil MOKHTARI, Amine HADDANE, Souleymane FALL, Nikola MILOSAVLJEVIC, Dina CHAOUKI, Rayan ZEBAZE SAO, Hugo RAGUIN) |
| **Story liée** | US-SC.1 (file asynchrone) · US-SC.2 (repli LLM managé UE) · US-SC.3 (ADR migration + cache/CDN + autoscaling) · US-SC.4 (FinOps) · épic E14 |

---

## 1. Contexte

Suite à un **passage TV**, EduTutor IA a failli s'effondrer sous la charge : l'architecture MVP (monolithe Django/DRF + Ollama sur un seul VPS) ne peut pas absorber des **millions d'utilisateurs simultanés**. L'État conditionne l'adoption nationale à une plateforme **fiable et élastique**. La levée de fonds finance la migration, mais le sponsor exige *« un plan clair, pas du code bricolé dans la panique »* (perturbation J4).

Deux contraintes non négociables héritées des ADR précédents restent en vigueur :
- **Souveraineté des données (RGPD)** — tout traitement de contenu cours reste en UE ([ADR-0001](adr-0001-choix-modele-llm.md)).
- **Sécurité de bout en bout** — la garde anti-injection reste active dans chaque worker ([ADR-0002](adr-0002-parade-prompt-injection.md)).

---

## 2. Options envisagées

| Option | Principe | Élasticité | RGPD | Complexité opé. | Verdict |
|---|---|:--:|:--:|:--:|---|
| **A. Statu quo** | Monolithe Django/DRF + Ollama, 1 VPS | ❌ nulle | ✅ | faible | ❌ effondrement prouvé |
| **B. Scale-up vertical** | VPS 64 cœurs / 256 Go RAM | 🟡 limitée | ✅ | faible | ❌ plafond dur, coût × 8, SPOF |
| **C. Scale-out horizontal — sans file** | Plusieurs réplicas Django/DRF stateless, load-balancer | 🟡 partielle | ✅ | moyenne | ❌ la génération LLM reste bloquante par requête |
| **D. Architecture asynchrone à files + workers + autoscaling** | API stateless · file de tâches (Redis/Celery) · pool de workers GPU · CDN pour assets statiques · autoscaling K8s ou Fly.io | ✅ élevée | ✅ (UE) | élevée | ✅ **retenu** |
| **E. Serverless pur (AWS Lambda / Vercel)** | Chaque requête = une fonction éphémère | ✅ infinie | ❌ hors UE possible | moyenne | ❌ Ollama incompatible (modèle local > 4 Go) ; transferts hors UE risqués |

---

## 3. Décision

> **Décision : adopter l'option D — architecture asynchrone à 4 composants découplés**, déployable de façon **incrémentale** (sans big bang) à partir du monolithe existant.
>
> ### Composant 1 — API stateless (Django/DRF)
> L'API **ne génère plus les quiz directement** : elle enfile une tâche dans la file et retourne immédiatement un `task_id`. Le client poll `/tasks/{id}` ou écoute via SSE. Cela supprime le blocage HTTP de 12 s par requête.
>
> ### Composant 2 — File de tâches (Redis + Celery)
> Chaque demande de génération est une tâche Celery sérialisée dans Redis. La file agit comme **tampon** : en pic de charge, les tâches s'accumulent au lieu de faire tomber l'API.
> Priorités possibles : quiz urgents > rebonds > exports.
>
> ### Composant 3 — Pool de workers GPU (autoscalé)
> Les workers Celery embarquent Ollama (`mistral:7b` par défaut, cf. ADR-0001). Chaque worker traite **1 tâche à la fois** (modèle local séquentiel). L'autoscaler (K8s HPA ou Fly.io Machine) ajoute/retire des workers selon la profondeur de file.
> **Repli LLM managé UE** (Mistral AI API, hébergement FR) activé par feature-flag `LLM_OVERFLOW_PROVIDER` quand la file dépasse un seuil configurable (US-SC.2) — conforme RGPD, aucun transfert hors UE.
>
> ### Composant 4 — Cache & CDN
> - **Cache Redis** des quiz déjà générés (clé = hash(cours + langue + nb_questions)) : évite de relancer Ollama pour un cours identique → gain immédiat sur les redoublants.
> - **CDN Bunny.net (UE)** pour les assets statiques (JS, CSS, images) : réduit la charge réseau du VPS principal.

---

## 4. Justification *(au-delà de « ça scale » — CA-J4-6)*

- **Découplage = résilience** : l'API répond en < 200 ms même si tous les workers sont occupés ; la file absorbe les pics sans SPOF.
- **Incrément ≠ big bang** : le monolithe peut coexister le temps de migrer — on branche Celery derrière l'endpoint `/api/llm/generate-quiz/` existant, sans réécrire le frontend ni la garde sécurité.
- **Contraintes respectées** : Ollama local en UE (RGPD) ; la garde `prompt_guard.py` est importée dans chaque worker (ADR-0002, DRY).
- **Repli sans régression** : le feature-flag `LLM_OVERFLOW_PROVIDER` permet de basculer sur Mistral UE **sans redéploiement** — décision réversible, conforme à l'esprit de l'ADR-0001.
- **FinOps maîtrisé** : le cache réduit les appels GPU ; les quotas Celery plafonnent le parc de workers ; Grafana/Prometheus mesurent le coût par quiz (US-SC.4).

---

## 5. Plan de migration incrémental

| Phase | Livrable | Périmètre | Sprint cible |
|:--:|---|---|:--:|
| **0** | ADR-0003 accepté *(ce document)* | Décision tracée | S6 (J4) |
| **1** | Branchement Celery/Redis + endpoint `/tasks/{id}` | API asynchrone, 1 worker local | S7 |
| **2** | Autoscaling workers GPU (K8s ou Fly.io) | Élasticité en charge | S7–S8 |
| **3** | Cache Redis quiz + CDN assets | Réduction charge & coût | S8 |
| **4** | Repli LLM managé UE (feature-flag) + observabilité | Filet de sécurité FinOps | S8 |

---

## 6. Conséquences

**Positives (+)**
- La plateforme peut absorber des pics (millions d'utilisateurs) sans effondrement.
- La génération de quiz passe de **bloquante** à **non-bloquante** : expérience utilisateur améliorée même sous charge.
- La décision est **réversible et tracée** — le sponsor dispose d'un plan clair (exigence J4).
- RGPD / souveraineté préservés à chaque phase.

**À surveiller (−)**
- **Complexité opérationnelle** accrue : Redis, Celery, workers GPU, autoscaler → nécessite une runbook et une formation DevOps (US-SC.4).
- **Consistance du cache** : si le cours évolue, la clé de cache doit changer → invalider par hash ou TTL court.
- **Coût de la file** en situation idle : Redis et le worker minimal tournent 24/7 → quota à définir (US-SC.4).
- **Tests de charge** à réaliser avant passage en production nationale (US-SC.1 : SLA ≤ 500 ms de réponse API + ≤ 30 s de génération en queue).

---

*ADR-0003 — équipe 6 · format Architecture Decision Record (1 page) · statut **Accepté** le 02/07/2026. Voir aussi [ADR-0001](adr-0001-choix-modele-llm.md) (choix LLM) · [ADR-0002](adr-0002-parade-prompt-injection.md) (sécurité) · [Perturbation J4](../../perturbations/j4-passage-echelle.md).*
