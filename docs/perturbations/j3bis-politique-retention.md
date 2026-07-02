# Perturbation J3-bis — Politique de rétention des données (RGPD)

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Sprint 5 (mercredi 14h–17h45) |
| **Artefact** | Perturbation J3-bis — Politique de conservation & purge |
| **Version** | v1.0 |
| **Date** | 01/07/2026 |
| **Statut** | ✅ Politique définie (purge automatisée : tâche `T-J3bis-purge` planifiée) |
| **Rédacteur** | Hugo RAGUIN |

> Liens : [Export RGPD (SAR)](j3bis-rgpd.md) · [`models.py`](../../backend/accounts/models.py) · [Product Backlog E8](../cadrage/product-backlog.md).

---

## 1. Principe (RGPD art. 5-1-e — limitation de la conservation)

Une donnée personnelle n'est conservée que **le temps nécessaire** à la finalité pour laquelle elle a été collectée, puis **supprimée ou anonymisée**. EduTutor IA collecte le **minimum** (email-identifiant, quiz de révision) et garde tout **en local** (souveraineté, LLM Ollama — cf. [ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md)).

## 2. Durées de conservation par donnée *(CA-J3bis-R1)*

| Donnée | Finalité | Durée de conservation | Purge / effacement |
|---|---|---|---|
| **Compte** (`User`, `Profile`) | Authentification, usage du service | Tant que le compte est **actif** | Sur demande : **hard delete immédiat** (art. 17) ; **compte inactif > 24 mois** → suppression automatique |
| **Quiz + Questions + réponses** (`Quiz`, `Question`) | Révision, historique de progression | Liés au compte | Cascade à la suppression du compte (`on_delete=CASCADE`) |
| **Trace de demande SAR** (`DataRequest`) | Accountability (prouver le traitement) | **12 mois** après la demande | Purge automatique au-delà |
| **Journal d'audit** (`AuditEvent`) | Accountability (export/suppression) | **12 mois** | Purge automatique au-delà ; cascade si compte supprimé |
| **Fichier d'export RGPD** | Portabilité (art. 20) | **0 — jamais archivé côté serveur** | Seule l'empreinte **SHA-256** est conservée (preuve d'intégrité) |
| **Tokens d'authentification** (DRF) | Session | Jusqu'au logout / changement de mot de passe | Invalidés immédiatement (`Token.delete()`) |
| **Logs applicatifs** (serveur) | Exploitation / sécurité | Courte durée (rotation) | Pas de donnée perso en clair (emails masqués dans les warnings) |

## 3. Mécanisme de purge *(CA-J3bis-R2)*

- **Suppression à la demande** (droit à l'effacement) : déjà en place — `DELETE /api/accounts/profile/` → hard delete + cascade.
- **Purge périodique** : commande de gestion planifiable `python manage.py purge_rgpd` (tâche **T-J3bis-purge**, à exécuter en cron quotidien) qui :
  1. supprime les `DataRequest` et `AuditEvent` de plus de 12 mois ;
  2. supprime (ou anonymise) les comptes **inactifs depuis > 24 mois**.
- **Non-archivage des exports** : garanti par conception dans [`exporting.py`](../../backend/accounts/exporting.py) (le fichier est streamé, jamais écrit sur disque serveur).

> État : la politique et les durées sont **actées** ; la commande `purge_rgpd` est planifiée (T-J3bis-purge). La suppression immédiate et le non-archivage des exports sont **déjà implémentés**.

## 4. Critères d'acceptation

- [x] **CA-J3bis-R1** — Durée de conservation définie **pour chaque donnée** perso → §2
- [x] **CA-J3bis-R2** — Mécanisme de purge décrit (à la demande + périodique) → §3
- [x] **CA-J3bis-R3** — Base légale citée (art. 5-1-e, minimisation) → §1
- [x] **CA-J3bis-R4** — Cohérent avec le code (cascade, non-archivage des exports, hard delete) → §2/§3
- [ ] **CA-J3bis-R5** — *Complément* : implémenter la commande `purge_rgpd` (T-J3bis-purge)

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Commentaire / preuve |
|---|:---:|---|
| Durée définie pour chaque donnée | ☑ Oui | §2 (tableau exhaustif). |
| Base légale RGPD citée | ☑ Oui | §1 (art. 5-1-e). |
| Mécanisme de purge décrit | ☑ Oui | §3 (demande + cron). |
| Cohérence avec le code | ☑ Oui | cascade, non-archivage export, hard delete. |
| Minimisation des données | ☑ Oui | email-identifiant + quiz uniquement, 100 % local. |

---

## 📚 Références

- **RGPD** art. 5-1-e (limitation de la conservation), art. 17 (effacement) — <https://www.cnil.fr/fr/les-durees-de-conservation-des-donnees>
- Sources internes : [Export RGPD (SAR)](j3bis-rgpd.md) · [ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md) · [Product Backlog E8](../cadrage/product-backlog.md).

---

*Perturbation J3-bis — politique de rétention de l'équipe 6. Durées + purge (à la demande et périodique). Complète l'[export RGPD](j3bis-rgpd.md).*
