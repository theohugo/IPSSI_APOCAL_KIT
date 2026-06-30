# Sprint Backlog — Sprint 1 — EduTutor IA

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Sprint 1 |
| **Artefact** | 7 sur 7 — Sprint Backlog |
| **Version** | v1.0 |
| **Date de remise** | 30/06/2026 |
| **Statut** | Draft (à valider PO) |
| **Rédacteur** | Amine HADDANE |
| **Fichier** | `equipe-6-sprint-backlog-v1.0` |

> Liens : [Product Backlog](product-backlog.md) · [Story Map](story-map.md) · [Customer Journey Map](03_customer_journey_map.md).

---

## 1. Objet du document

Le **Sprint Backlog** décompose les user stories tirées du [Product Backlog](product-backlog.md) en **tâches techniques atomiques (1–3 h)**, assignées et estimées, pour le **Sprint 1**. Mentalité **brownfield** : le kit fourni étant une base partielle, les tâches consistent surtout à **fiabiliser, brancher front↔back et tester** l'existant — pas à coder de zéro.

> **Format** : 3 à 5 tâches par story · estimation en **heures** (plus fin que les story points pour un sprint court) · « Restant » mis à jour à chaque daily.

---

## 2. Métadonnées du sprint

| | |
|---|---|
| **Numéro** | Sprint 1 |
| **Fenêtre** | Lundi 30/06/2026, 14h00 → 18h00 (4 h) |
| **Équipe** | 7 personnes |
| **Capacité** | 7 × 4 h = **28 h-personnes** |
| **Vélocité cible** | 13–16 SP (stories F1/F2 partielles) |
| **Scrum Master** | Hugo RAGUIN |
| **Product Owner** | Dina CHAOUKI *(proxy ; arbitrage final intervenant)* |

### 🎯 Sprint Goal
> **Fiabiliser le début du parcours** : un·e étudiant·e peut **s'inscrire, valider son email, se connecter, réinitialiser son mot de passe**, puis **déposer un cours** (PDF ≤ 5 Mo ou texte ≥ 200 car.) **validé**. Chaîne F1 + F2 robuste et **démontrable en Sprint Review à 18h**.

---

## 3. Stories engagées (depuis le Product Backlog)

| US | Intitulé | MoSCoW | SP | État initial |
|---|---|:--:|:--:|:--:|
| US-F1.3 | Valider son email via un lien | 🔴 M | 3 | 🔧 |
| US-F1.4 | Réinitialiser son mot de passe oublié | 🔴 M | 3 | 🔧 |
| US-F2.1 | Téléverser un PDF (≤ 5 Mo) | 🔴 M | 5 | 🔧 |
| US-F2.2 | Coller du texte (≥ 200 car.) | 🔴 M | 2 | 🔧 |
| US-F2.3 | Message d'erreur si fichier trop lourd / texte trop court | 🔴 M | 2 | ⬜ |

---

## 4. Décomposition en tâches techniques

| US | ID tâche | Tâche technique | Type | Assigné | Estim. (h) | Restant (h) | Statut |
|---|---|---|---|---|:--:|:--:|---|
| — | T-0.1 | `docker compose up` : vérifier les 4 services (backend, frontend, postgres, ollama) sur chaque poste | Setup | Tous | 1 | 1 | Todo |
| — | T-0.2 | Mettre à jour le GitHub Project (colonnes, assignation des issues du sprint) | Setup | Hugo RAGUIN | 1 | 1 | Todo |
| US-F1.3 | T-1.3.1 | Fiabiliser l'endpoint `verify-email/` (token, expiration 24h, idempotence) | Back | Souleymane FALL | 2 | 2 | Todo |
| US-F1.3 | T-1.3.2 | Bouton « Renvoyer l'email » + rendre `VerifyEmailBanner` visible/non ignorable | Front | Nikola MILOSAVLJEVIC | 2 | 2 | Todo |
| US-F1.3 | T-1.3.3 | Tests flux validation (pytest endpoint + Vitest composant) | Test | Amine HADDANE | 2 | 2 | Todo |
| US-F1.4 | T-1.4.1 | Tester `password-reset/` de bout en bout, corriger le lien de reset | Back | Souleymane FALL | 2 | 2 | Todo |
| US-F1.4 | T-1.4.2 | Page front reset + validation mot de passe ≥ 8 caractères + messages | Front | Nikola MILOSAVLJEVIC | 2 | 2 | Todo |
| US-F2.1 | T-2.1.1 | Fiabiliser l'extraction `pypdf` + avertir si < 500 caractères extraits | Back | Kahil MOKHTARI | 3 | 3 | Todo |
| US-F2.1 | T-2.1.2 | Détecter PDF scanné/image → message « collez le texte » (prépare US-F2.4) | Back | Kahil MOKHTARI | 2 | 2 | Todo |
| US-F2.1 | T-2.1.3 | `UploadPage.tsx` : dropzone + retour « X pages / Y caractères extraits » | Front | Rayan ZEBAZE SAO | 2 | 2 | Todo |
| US-F2.2 | T-2.2.1 | Renforcer la validation texte ≥ 200 car. + compteur de caractères live | Front | Dina CHAOUKI | 1 | 1 | Todo |
| US-F2.3 | T-2.3.1 | Validation taille ≤ 5 Mo (back + front) + UX d'erreur claire | Full | Dina CHAOUKI | 2 | 2 | Todo |
| US-F2.x | T-2.x.1 | Tests upload (pytest extraction + Vitest formulaire) + section README | Test | Rayan ZEBAZE SAO | 2 | 2 | Todo |

**TOTAL : 26 h estimées** · capacité **28 h-pers** · marge ~2 h pour le pair-programming, l'onboarding et les imprévus.

> **Definition of Done (rappel)** : PR revue par un pair · CI verte · critères d'acceptation satisfaits · aucune régression · fonctionne sous Docker Compose · pas de secret en clair · commits Conventional Commits.

---

## 5. Burndown — Sprint 1

| Moment (daily / point d'étape) | Restant idéal (h) | Restant réel (h) | Δ réel-idéal |
|---|:--:|:--:|:--:|
| 14h00 (début) | 26 | 26 | 0 |
| 15h00 | 19 | _à reporter_ | — |
| 16h00 | 13 | _à reporter_ | — |
| 17h00 | 6 | _à reporter_ | — |
| 18h00 (review) | 0 | _à reporter_ | — |

> **Lecture** : descente cible quasi linéaire de 26 h → 0 h. Si « réel » > « idéal » sur deux points consécutifs → **alerte capacité**, à arbitrer en daily (retirer une Should, ou renforcer une tâche bloquée).

---

## 6. Statuts & rituels

| Statut | Signification |
|---|---|
| **Todo** | Tâche pas encore commencée |
| **In Progress** | En cours (idéalement 1 seule par personne) |
| **Blocked** | Bloquée → à remonter au daily |
| **Done** | Terminée **et** validée (DoD respectée) |

- **Daily** : court point à 15h / 16h / 17h (sprint de 4 h) → mise à jour du « Restant » et du burndown.
- **Sprint Review** : 18h, démo du parcours inscription → dépôt de cours au PO.
- **Sprint Retrospective** : courte rétro en fin de journée (ce qui a marché / à améliorer).

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Commentaire / preuve |
|---|:---:|---|
| Le sprint a un objectif (Sprint Goal) clair et démontrable | ☑ Oui | §2 : chaîne F1+F2 fiabilisée, démontrable en review. |
| Les métadonnées (durée, capacité, vélocité, rôles) sont renseignées | ☑ Oui | §2 : 28 h-pers, SM/PO, fenêtre 14h-18h. |
| Les stories engagées proviennent du Product Backlog | ☑ Oui | §3 : US-F1.3/F1.4/F2.1/F2.2/F2.3 tracées. |
| Chaque story est décomposée en 3-5 tâches atomiques (1-3 h) | ☑ Oui | §4 : tâches T-x.y assignées + estimées. |
| Les tâches sont assignées nominativement aux 7 membres | ☑ Oui | §4 : colonne « Assigné ». |
| L'estimation (h) tient dans la capacité du sprint | ☑ Oui | 26 h estimées < 28 h-pers (marge documentée). |
| Un suivi (burndown) est prévu | ☑ Oui | §5 burndown + dailies. |
| La Definition of Done est rappelée | ☑ Oui | §4 encart DoD. |
| Le document a été relu et validé par l'équipe | ☑ Oui | Revue d'équipe avant remise · validation PO en attente. |

---

## 📚 Références

- Scrum Guide officiel FR — scrumguides.org (Sprint Backlog, Sprint Goal, événements)
- Cours Agile/Scrum (Mohamed EL AFRIT) — mohamedelafrit.com/teaching/APOCALIPSSI
- Sources internes : [Product Backlog](product-backlog.md) · [Story Map](story-map.md) · [Customer Journey Map](03_customer_journey_map.md)

---

## 🔄 Convention de versionnement

- **v1.0** — sprint backlog initial du Sprint 1 (30/06/2026)
- **v1.x** — mises à jour quotidiennes (statuts, restant, burndown) pendant le sprint
- **v2.0** — nouveau sprint (Sprint 2, etc.) ou refonte suite à une perturbation

---

*Sprint Backlog du Sprint 1 — décomposition technique tracée sur le Product Backlog de l'équipe 6, ancrée dans l'existant (brownfield).*
*Dépôt : `/docs/cadrage/sprint-backlog.md` — v1.0 — 30/06/2026*
