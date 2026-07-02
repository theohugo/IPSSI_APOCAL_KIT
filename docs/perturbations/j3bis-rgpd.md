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

**M. Hugo Petit** (étudiant M2 Droit numérique) soumet le **mercredi 10h30**, en pleine livraison MVP, une **demande formelle d'accès** (RGPD **Art. 15**) : il réclame l'export complet de ses données (compte, cours/textes, quiz, réponses et scores, signalements, logs d'audit) en **format structuré (JSON ou CSV)**, avec un **délai de réponse de 48 h**. En parallèle, l'obligation d'afficher les **mentions légales, CGU, confidentialité et cookies** s'applique. Il faut une réponse **outillée** (pas un traitement manuel).

> Reformulation (1 phrase) : *« Tout utilisateur doit pouvoir, en un clic, télécharger l'intégralité de ses données personnelles dans un format lisible par machine, et consulter les pages légales du service. »*
>
> Nature de la perturbation : **arbitrage documentaire** (priorisation, registre de traitement) plus qu'un sprint de code. Livrables : endpoint + bouton + politique de rétention + audit trail + **réponse écrite** au demandeur.

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

## 3. API + IHM livrées *(CA-J3bis-2)*

| Méthode | Route | Rôle |
|---|---|---|
| `GET` | **`/api/accounts/me/export/`** | **Endpoint canonique** (énoncé J3-bis) : génère et **télécharge** l'export (`?fmt=json` ou `zip`). Trace un `DataRequest` + `AuditEvent`. |
| `GET` | `/api/accounts/data-export/` | Renvoie l'**historique** des demandes d'export de l'utilisateur. |
| `POST` | `/api/accounts/data-export/` | Variante génération/téléchargement (compat). |

- **Bouton frontend** : *Mon profil → Mes données → **« Exporter mes données (JSON) »*** (+ ZIP) — [`ProfilePage.tsx`](../../frontend/src/pages/ProfilePage.tsx) via [`exportMyData`](../../frontend/src/api/auth.ts).
- **6 catégories** exportées : compte, quiz (cours + questions), réponses, **signalements**, demandes d'accès, journal d'audit.
- **Authentification obligatoire** (`IsAuthenticated`) : un anonyme reçoit 401/403 (`test_me_export_requires_auth`).
- **Empreinte** : l'export n'est **pas** archivé côté serveur ; seul son `sha256` est conservé (preuve d'intégrité sans re-stocker la donnée).
- **Modèle de données** : `DataRequest` (statut `processing → responded / failed`, format, taille, hash) et `AuditEvent` (type `data_export` / `account_deleted`) — migration `0002_auditevent_datarequest`.
- **Réponse écrite** au demandeur : [réponse à M. Hugo Petit](j3bis-reponse-hugo-petit.md).

---

## 4. Critères d'acceptation J3-bis

- [x] **CA-J3bis-1** — Endpoint **`GET /api/accounts/me/export/`** → 200 + données structurées → §3
- [x] **CA-J3bis-2** — Export **complet 6 catégories** (compte, quiz, réponses, signalements, demandes, audit) → §2/§3
- [x] **CA-J3bis-3** — **≥ 2 formats** (JSON + ZIP), lisibles par machine → §3
- [x] **CA-J3bis-4** — **Bouton frontend** « Exporter mes données » (profil authentifié) → [`ProfilePage.tsx`](../../frontend/src/pages/ProfilePage.tsx)
- [x] **CA-J3bis-5** — **Politique de rétention** écrite (≥ 3 sections) → [politique de rétention](j3bis-politique-retention.md)
- [x] **CA-J3bis-6** — **Audit trail** `DataRequest` en base (qui, quand, statut, hash) → [`models.py`](../../backend/accounts/models.py)
- [x] **CA-J3bis-7** — **Réponse professionnelle** au demandeur (M. Hugo Petit) → [email](j3bis-reponse-hugo-petit.md)
- [x] *Bonus* — Isolation inter-comptes + accès authentifié + pages légales → tests + `frontend/src/pages/legal/`

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
