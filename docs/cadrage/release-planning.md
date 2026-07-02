# Release Planning — EduTutor IA

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Cadrage (avant Sprint 1) |
| **Artefact** | 5 sur 7 — Release Planning |
| **Version** | v1.0 |
| **Date de remise** | 30/06/2026 |
| **Statut** | Draft (à valider PO) |
| **Rédacteur** | Rayan ZEBAZE SAO |
| **Fichier** | `equipe-6-release-planning-v1.0` |

> Liens : [Story Map](story-map.md) · [Product Backlog](product-backlog.md) · [Sprint Backlog](sprint-backlog.md).

---

## 1. Objet du document

Placer les user stories de la [Story Map](story-map.md) sur les **8 sprints de demi-journée** de la semaine immersive. Les identifiants `US-Fx.x` / `US-T.x` / `US-Rx.x` renvoient directement au [Product Backlog](product-backlog.md) (traçabilité unique sur tout le cadrage).

**Jalons imposés :**
- 🎯 **Release 1 (MVP F1–F6 + espace enseignant)** livrée fin de **Sprint S5 — mercredi 17h45**.
- 🚀 **Release 2** (pistes retenues) livrée fin de **Sprint S7 — jeudi 17h45**.
- 🏛️ **Release 3 « Plateforme publique »** (RGAA · i18n · scalabilité) cadrée en J4, planifiée au-delà de la semaine.
- 🎤 **Soutenance** : vendredi.

> **Règle J1** : le **Sprint 1 est volontairement sous-engagé (~70 % de la capacité)** car la vélocité réelle de l'équipe est encore inconnue. Les sprints suivants seront recalibrés à partir de la vélocité observée (cf. §3 Burnup).

---

## 2. Planning des 8 sprints

| Sprint | Période | Capacité (h-pers) | Vélocité visée (SP) | Objectif | Stories (Product Backlog) | Perturbation | Release / Jalon |
|:--:|---|:--:|:--:|---|---|---|---|
| **S1** | Lun 29/06 · 14h–18h | 28 | 14 | Fiabiliser l'auth (validation email, reset) + premier dépôt de cours | US-F1.3, US-F1.4, US-F2.1, US-F2.2, US-F2.3 | — | Sprint 1 (cadrage → code) |
| **S2** | Mar 30/06 · 09h–13h | 28 | 18 | Dépôt robuste + génération quiz LLM local stable | US-F2.4, US-F3.1, US-F3.4 | J1 *(lun. 14h, traitée mar. 9h)* : persona Mme Lefèvre | — |
| **S3** | Mar 30/06 · 14h–18h | 28 | 20 | Décision technique : benchmark LLM, **ADR** fournisseur, RAG ancré | US-X.3, US-F3.5, US-F3.3 | J2 *(mar. 10h)* : latence / choix modèle | — |
| **S4** | Mer 01/07 · 09h–13h | 28 | 20 | Durcir correction + score, premiers tests de sécurité adversariaux | US-F4.1, US-F5.1, US-F5.2, US-S.1, US-S.2 | J3 *(mer. 10h)* : prompt injection | — |
| **S5** | Mer 01/07 · 14h–17h45 | 24 | 22 | Historique + RGPD + **espace enseignant** + stabiliser le MVP | US-F6.1, US-G.1, US-G.2, US-T.1, US-T.2, US-T.3 | J3-bis *(mer. 14h)* : SAR RGPD / pages légales | 🎯 **RELEASE 1 — MVP** (tag `v1.0.0-mvp`) — Mer 17h45 |
| **S6** | Jeu 02/07 · 09h–13h | 28 | 18 | Absorber J4 : analyser les risques, reprioriser, cadrer RGAA/i18n/scalabilité | SPK-5, US-A11Y.1, US-SC.3, US-I18N.1 | J4 *(jeu. 10h)* : passage à l'échelle / plateforme d'État | — |
| **S7** | Jeu 02/07 · 14h–17h45 | 24 | 18 | Finaliser R2 et figer le plan Release 3 « Plateforme publique » | US-R2.6, US-R2.2, US-SC.1, US-A11Y.2 | J4 suite : backlog préventif + burnup actualisé | 🚀 **RELEASE 2** (tag `v1.1.0`) — Jeu 17h45 |
| **S8** | Ven 03/07 · matin | 20 | 10 | Stabilisation finale, runbook, répétition de la démo, préparation soutenance avec impact J4 | US-D.3, US-D.5, US-X.1, US-SC.4 | — | 🎤 **Soutenance** (vendredi) |
| **TOTAL** | Semaine complète | **208** | **140** | | | | |

> ⚠️ **Anti-piège vélocité** : S1 sous-engagé (~70 %). Les vélocités de S2+ sont indicatives et seront **recalibrées après chaque rétro** selon le débit réel.

---

## 3. Burnup global (story points cumulés)

| Sprint | Date | SP planifiés (cumulé) | SP livrés (cumulé) | Périmètre total | Écart | Jalon |
|:--:|---|:--:|:--:|:--:|:--:|---|
| S1 | Lun 29/06 | 14 | _à compléter_ | 140 | — | Sprint 1 |
| S2 | Mar 30/06 | 32 | _à compléter_ | 140 | — | — |
| S3 | Mar 30/06 | 52 | _à compléter_ | 140 | — | — |
| S4 | Mer 01/07 | 72 | _à compléter_ | 140 | — | — |
| S5 | Mer 01/07 | 94 | _à compléter_ | 140 | — | 🎯 Release 1 |
| S6 | Jeu 02/07 | 112 | _à compléter_ | 140 | — | J4 révélé : cadrage en cours |
| S7 | Jeu 02/07 | 130 | _à compléter_ | **209** | +68 pts J4 | 🚀 Release 2 + plan R3 |
| S8 | Ven 03/07 | 140 | _à compléter_ | 209 | R3 au-delà semaine | 🎤 Soutenance |

> À chaque fin de sprint : reporter les **SP réellement terminés** (Definition of Done respectée) dans « SP livrés (cumulé) » et recalculer l'écart. Si l'écart se creuse → arbitrage PO (retirer des Should, recadrer le périmètre).
> **Mise à jour J4** : le burnup matérialise le saut de périmètre **141 → 209 points** (+68 pts, +48 %) ; les stories RGAA/i18n/scalabilité basculent en **Release 3** au lieu de dégrader l'engagement R2.

---

## 4. Légende & hypothèses

**Jalons** : 🎯 Release 1 (MVP F1–F6 + espace enseignant, `v1.0.0-mvp`, mer. 17h45 strict) · 🚀 Release 2 (`v1.1.0`, jeu. 17h45 strict) · 🏛️ Release 3 « Plateforme publique » (cadrée J4, au-delà semaine) · 🎤 Soutenance (vendredi).

**Capacité** : équipe de **7 personnes** · ~**28 h-pers** par demi-journée pleine (7 × 4 h), réduite à **24/20 h-pers** sur les sprints raccourcis (S5, S7, S8).

**Conversion h-pers → SP** : indicative (pas de ratio fixe), à affiner avec les estimations du [Product Backlog](product-backlog.md).

**Perturbations** : les 5 perturbations pédagogiques (J1→J4 + J3-bis) sont rattachées au sprint qui les absorbe ; chacune a un **spike de préparation** (SPK-1 à SPK-5) dans le [Product Backlog](product-backlog.md) §6.

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Commentaire / preuve |
|---|:---:|---|
| Les sprints couvrent toute la semaine avec capacité chiffrée | ☑ Oui | §2 : 8 sprints, 208 h-pers au total. |
| Chaque sprint a un objectif clair | ☑ Oui | Colonne « Objectif ». |
| Les stories sont tracées vers le Product Backlog (IDs réels) | ☑ Oui | US-Fx.x / US-T.x / US-Rx.x cohérents avec backlog et story map. |
| Les jalons Release 1 / Release 2 / Release 3 sont datés et positionnés | ☑ Oui | R1 fin S5, R2 fin S7, R3 cadrée J4 et planifiée au-delà semaine. |
| La règle de sous-engagement du Sprint 1 est appliquée | ☑ Oui | S1 = 14 SP (~70 %). |
| Les perturbations sont rattachées aux sprints | ☑ Oui | Colonne « Perturbation » (J1→J4, J3-bis). |
| Un suivi (burnup) est prévu | ☑ Oui | §3 burnup cumulé + saut J4 à 209 pts. |
| Le document a été relu et validé par l'équipe | ☑ Oui | Revue d'équipe avant remise · validation PO en attente. |

---

## 📚 Références

- Scrum Guide officiel FR — scrumguides.org (release planning, vélocité, burn-up)
- Cours Agile/Scrum (Mohamed EL AFRIT) — mohamedelafrit.com/teaching/APOCALIPSSI
- Sources internes : [Story Map](story-map.md) · [Product Backlog](product-backlog.md) · [Sprint Backlog](sprint-backlog.md)

---

## 🔄 Convention de versionnement

- **v1.0** — release planning initial du cadrage, source Markdown (30/06/2026), identifiants alignés sur le Product Backlog
- **v1.x** — recalibrage des vélocités après chaque rétro / mise à jour du burnup
- **v2.0** — refonte majeure suite à une perturbation (changement de périmètre ou de jalon)

---

*Release Planning de l'équipe 6 — 8 sprints de demi-journée, tracé sur le Product Backlog et la Story Map.*
*Dépôt : `/docs/cadrage/release-planning.md` — v1.0 — 30/06/2026*
