# Perturbation J3-bis — RGPD : droit d'accès et à la portabilité (SAR)

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Sprint 5 (mercredi 14h–17h45) |
| **Artefact** | Perturbation J3-bis — Export RGPD + pages légales |
| **Version** | v1.0 |
| **Date** | 01/07/2026 |
| **Statut** | ✅ Validé (endpoint d'export livré + 6 tests verts ; pages légales en ligne) |
| **Rédacteur** | Hugo RAGUIN |

> Liens : [Product Backlog](../cadrage/product-backlog.md) (E7/E8 sécurité & RGPD) · [Release Planning §S5](../cadrage/release-planning.md) · Code : [`exporting.py`](../../backend/accounts/exporting.py) · [`views.py`](../../backend/accounts/views.py) · [`models.py`](../../backend/accounts/models.py) · Pages légales : [`frontend/src/pages/legal/`](../../frontend/src/pages/legal/).
> Source : énoncé du cours — <https://mohamedelafrit.com/teaching/APOCALIPSSI/pages/perturbations/j3bis-rgpd.php>

---

## 1. Scénario

Un utilisateur exerce ses droits RGPD : **« Quelles données avez-vous sur moi, et rendez-les moi dans un format réutilisable »** (droit d'accès — art. 15 — et à la portabilité — art. 20). En parallèle, le sponsor rappelle l'obligation d'afficher les **mentions légales, CGU, politique de confidentialité et cookies**. Il faut une réponse **outillée** (pas un email manuel) avant la Release 1.

> Reformulation (1 phrase) : *« Tout utilisateur doit pouvoir, en un clic, télécharger l'intégralité de ses données personnelles dans un format lisible par machine, et consulter les pages légales du service. »*

---

## 2. Réponse livrée *(CA-J3bis-1)*

| Exigence RGPD | Réponse EduTutor IA | Preuve |
|---|---|---|
| **Droit d'accès (art. 15)** | Endpoint qui rassemble compte + profil + quiz + réponses + historique | [`exporting.build_export_payload`](../../backend/accounts/exporting.py) |
| **Portabilité (art. 20)** | Export **JSON** (défaut) ou **ZIP** (un fichier par catégorie), format machine | [`build_export_artifact`](../../backend/accounts/exporting.py) |
| **Minimisation / isolation** | L'export ne contient **que** les données de l'utilisateur connecté (testé) | `test_data_export_isolates_other_users` |
| **Accountability** | Chaque demande tracée (`DataRequest`) + événement d'audit (`AuditEvent`), avec empreinte SHA-256 de l'export | [`models.py`](../../backend/accounts/models.py), [`audit.py`](../../backend/accounts/audit.py) |
| **Droit à l'effacement (art. 17)** | Suppression de compte (hard delete, cascade) — l'export est proposé **en amont** | [`views.ProfileView.delete`](../../backend/accounts/views.py) |
| **Souveraineté des données** | LLM **local** (Ollama) : aucune donnée personnelle envoyée au cloud (cf. ADR-0001) | [ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md) |
| **Transparence** | Pages **Mentions légales / CGU / Confidentialité / Cookies** | [`frontend/src/pages/legal/`](../../frontend/src/pages/legal/) |

---

## 3. API livrée *(CA-J3bis-2)*

| Méthode | Route | Rôle |
|---|---|---|
| `POST` | `/api/accounts/data-export/` | Génère et **télécharge** l'export (`?format=json` ou `zip`). Trace un `DataRequest` + `AuditEvent`. |
| `GET` | `/api/accounts/data-export/` | Renvoie l'**historique** des demandes d'export de l'utilisateur. |

- **Authentification obligatoire** (`IsAuthenticated`) : un anonyme reçoit 401/403 (`test_data_export_requires_auth`).
- **Empreinte** : l'export n'est **pas** archivé côté serveur ; seul son `sha256` est conservé (preuve d'intégrité sans re-stocker la donnée).
- **Modèle de données** : `DataRequest` (statut `processing → responded / failed`, format, taille, hash) et `AuditEvent` (type `data_export` / `account_deleted`) — migration `0002_auditevent_datarequest`.

---

## 4. Critères d'acceptation J3-bis

- [x] **CA-J3bis-1** — Export **complet** des données perso (compte, quiz, réponses) → §2
- [x] **CA-J3bis-2** — Format **lisible par machine** (JSON/ZIP), téléchargeable → §3
- [x] **CA-J3bis-3** — **Isolation** stricte : aucune donnée d'un autre utilisateur → `test_data_export_isolates_other_users`
- [x] **CA-J3bis-4** — Demande **tracée** (DataRequest) + audit (AuditEvent) → §2/§3
- [x] **CA-J3bis-5** — Accès **authentifié** uniquement → `test_data_export_requires_auth`
- [x] **CA-J3bis-6** — **Pages légales** en ligne (mentions, CGU, confidentialité, cookies) → `frontend/src/pages/legal/`
- [x] **CA-J3bis-7** — Tests automatisés (6) en CI → [`accounts/tests.py`](../../backend/accounts/tests.py)

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Commentaire / preuve |
|---|:---:|---|
| Besoin RGPD reformulé en 1 phrase | ☑ Oui | §1 (télécharger toutes ses données en 1 clic). |
| Droits d'accès + portabilité couverts | ☑ Oui | §2 (art. 15 & 20). |
| Format lisible par machine (JSON/ZIP) | ☑ Oui | §3 + `build_export_artifact`. |
| Isolation des données (pas de fuite inter-comptes) | ☑ Oui | test dédié. |
| Traçabilité / accountability | ☑ Oui | DataRequest + AuditEvent + SHA-256. |
| Pages légales publiées | ☑ Oui | 4 pages front. |
| Tests automatisés (CI) | ☑ Oui | 6 tests `accounts/tests.py`. |

---

## 5. Traçabilité

- **Épics** : E7 (Sécurité & durcissement), E8 (RGPD) — [Product Backlog](../cadrage/product-backlog.md).
- **Code** : [`exporting.py`](../../backend/accounts/exporting.py), [`audit.py`](../../backend/accounts/audit.py), [`models.py`](../../backend/accounts/models.py) (`DataRequest`, `AuditEvent`), [`views.py`](../../backend/accounts/views.py) (`DataExportView`).
- **Migration** : `accounts/migrations/0002_auditevent_datarequest.py`.
- **Tests** : [`accounts/tests.py`](../../backend/accounts/tests.py) (section J3-bis).

---

## 📚 Références

- **RGPD** — art. 15 (droit d'accès), art. 17 (effacement), art. 20 (portabilité) — <https://www.cnil.fr/fr/reglement-europeen-protection-donnees>
- **CNIL** — droit d'accès aux données — <https://www.cnil.fr/fr/le-droit-dacces>
- Sources internes : [ADR-0001](../cadrage/adr/adr-0001-choix-modele-llm.md) (LLM local = souveraineté) · [Product Backlog](../cadrage/product-backlog.md) (E7/E8).

---

*Perturbation J3-bis — export RGPD (SAR) de l'équipe 6 : endpoint d'export JSON/ZIP + traçabilité (DataRequest/AuditEvent) + pages légales. Complète la perturbation **J3** (injection de prompt).*
