# Story Map — EduTutor IA

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Cadrage |
| **Artefact** | 4 sur 7 — Story Map |
| **Version** | v1.0 |
| **Date de remise** | 30/06/2026 |
| **Statut** | Draft (à valider PO) |
| **Rédacteur** | Nikola MILOSAVLJEVIC |
| **Fichier** | `equipe-6-story-map-v1.0` |
| **Méthode** | Story Mapping (Jeff Patton) — carte 2D : activités × MoSCoW |

> Liens : [Product Vision Board](product-vision-board.md) · [Personas](personas.md) · [Customer Journey Map](03_customer_journey_map.md) · [Product Backlog](product-backlog.md) · [Perturbation J1](perturbations/j1-produit.md).

---

## 1. Objet du document

La **Story Map** (Jeff Patton) déroule le produit en **2 dimensions** :

- **Axe horizontal — le « backbone »** : les **activités utilisateur** dans l'ordre du parcours (de gauche à droite, cf. [Customer Journey](03_customer_journey_map.md)).
- **Axe vertical — la priorisation MoSCoW** : ce qu'on livre d'abord (**Must / Release 1**) en haut, le reste en dessous (**Should / Could / Won't**).

Chaque cellule pointe vers une **user story de notre [Product Backlog](product-backlog.md)** (traçabilité directe), avec son **état réel dans le code** (mentalité *brownfield*) :

> **Légende état** : ✅ livré (à recalibrer) · 🔧 partiel (à fiabiliser) · ⬜ à faire

**Spécificité Équipe 6** : conformément à notre positionnement *enseignant-first* et à la **perturbation J1**, le backbone inclut une **7ᵉ activité « Piloter sa classe »** (enseignante Mme Lefèvre) que les parcours purement étudiants n'ont pas.

**Mise à jour J4** : le passage à l'échelle ajoute une **8ᵉ activité transverse « Utiliser la plateforme publique »**. Elle ne remplace pas le parcours MVP ; elle ajoute les exigences nécessaires pour une adoption nationale : **RGAA**, **i18n** et **scalabilité**.

---

## 2. Backbone — Activités utilisateur (epics)

| # | Activité utilisateur | Epic backlog | Persona |
|:--:|---|---|---|
| 1 | **S'inscrire & gérer son compte** | E1 / E8 | Lucas, Léa, Karim |
| 2 | **Déposer un cours** | E2 | Lucas, Léa, Karim |
| 3 | **Générer un quiz** | E3 | Lucas, Léa, Karim |
| 4 | **Passer le quiz & être corrigé** | E4 | Lucas, Léa, Karim |
| 5 | **Consulter ses résultats** | E5 | Lucas, Léa, Karim |
| 6 | **Suivre sa progression** | E6 | Karim (régulier) |
| 7 | **Piloter sa classe** *(enseignant·e — J1)* | E11 / espace enseignant | Mme Lefèvre |
| 8 | **Utiliser la plateforme publique** *(J4)* | E14 / E15 / E16 | Amina, Diego, État / DPO |

---

## 3. Carte 2D — Activités × MoSCoW

> Lecture : chaque ligne est un **niveau de priorité** ; chaque colonne une **activité**. La **ligne MUST** = le **MVP Release 1** (squelette ambulant : s'inscrire → déposer → générer → passer → résultats → historique).

| MoSCoW ↓ \ Activité → | 1. S'inscrire & compte | 2. Déposer un cours | 3. Générer un quiz | 4. Passer & corriger | 5. Résultats | 6. Progression | 7. Piloter sa classe |
|---|---|---|---|---|---|---|---|
| **🔴 MUST**<br>*(Release 1)* | US-F1.1 ✅<br>US-F1.2 ✅<br>US-F1.3 🔧<br>US-F1.4 🔧<br>US-F1.5 ✅<br>US-G.1 ⬜ · US-G.2 🔧 | US-F2.1 🔧<br>US-F2.2 🔧<br>US-F2.3 ⬜ | US-F3.1 🔧<br>US-F3.2 ✅<br>US-F3.4 ⬜ | US-F4.1 🔧<br>US-F4.2 ✅ | US-F5.1 🔧<br>US-F5.2 🔧 | US-F6.1 🔧 | US-T.1 ⬜<br>US-T.2 ⬜<br>US-T.3 ⬜ |
| **🟠 SHOULD**<br>*(R1 si le temps le permet)* | US-F1.6 ⬜<br>US-G.3 ⬜ · US-G.4 ⬜ | US-F2.4 ⬜ | US-F3.3 ⬜<br>US-F3.5 🔧 | — | US-F5.3 ⬜ *(landing)* | US-F6.2 🔧 | — |
| **🟡 COULD**<br>*(Release 2)* | US-G.5 ⬜ *(export RGPD)* | — | US-R2.1 🔧 *(RAG renforcé)*<br>US-R2.3 ⬜ *(difficulté)* | — | US-R2.4 ⬜ *(explications)*<br>US-FB.1 ⬜ *(noter quiz)* | US-F6.3 ⬜ *(filtres)*<br>US-R2.5 ✅ · US-R2.6 ✅ | US-R2.2 ⬜ *(dashboard prof + export)* |
| **⚪ WON'T**<br>*(hors semaine)* | US-W.2 *(paiement)* | US-W.3 *(LLM cloud par défaut — RGPD)* | — | — | US-FB.2 *(signalement)* | US-W.1 *(app mobile native)* | — |

---

## 4. Tranches de livraison (release slices)

| Slice | Contenu | Échéance |
|---|---|---|
| **🥇 Walking skeleton (MVP)** | Toute la **ligne MUST** : parcours complet s'inscrire → déposer → générer → passer → résultats → historique **+ espace enseignant** (US-T.x) | **Mercredi 17h45 (R1)** |
| **🥈 Confort R1** | Stories **SHOULD** insérées si la vélocité le permet (messages d'erreur, RAG ancré, landing) | Mercredi, si capacité |
| **🥉 Release 2** | Stories **COULD** (RAG renforcé, explications, dashboard enseignant) arbitrées par le PO | **Jeudi soir (R2)** |
| **🏛️ Release 3 — Plateforme publique** | Passage à l'échelle J4 : scalabilité nationale (US-SC.*), accessibilité RGAA (US-A11Y.*), i18n (US-I18N.*), conformité internationale (US-RGPD-INT.1) | Cadrée jeudi, planifiée au-delà de la semaine |

> **Risque n°1 (cf. backlog §9)** : la chaîne **US-F3.1 → US-F4.1 → US-F5.1 → US-F6.1** est majoritairement en 🔧. C'est le **chemin critique du MVP** : à fiabiliser en priorité, sinon pas de démo.

---

## 4bis. Addendum J4 — Activité transverse « Plateforme publique »

| Axe J4 | Activité utilisateur | Stories backlog | MoSCoW |
|---|---|---|:--:|
| **Scalabilité** | Générer un quiz même en période de pic national, sans timeout ni file bloquante visible. | US-SC.1, US-SC.2, US-SC.3, US-SC.4 | M/M/S/C |
| **Accessibilité RGAA** | Naviguer au clavier, lire l'interface au lecteur d'écran, comprendre les erreurs et focus. | US-A11Y.1, US-A11Y.2 | M/S |
| **Internationalisation** | Choisir une langue d'interface et obtenir des quiz IA cohérents dans cette langue. | US-I18N.1, US-I18N.2 | S/S |
| **Conformité internationale** | Garantir hébergement UE, DPA et absence de transfert non maîtrisé. | US-RGPD-INT.1 | M |

> Lecture PO : ces stories sont **préventives**. Elles réduisent les risques J4 identifiés dans [j4-passage-echelle.md](../perturbations/j4-passage-echelle.md) et ne doivent pas être confondues avec le périmètre de démonstration R1/R2.

---

## 5. Visualisation (synthèse)

```
ACTIVITÉS →  1.Compte   2.Cours   3.Générer  4.Passer  5.Résultats 6.Progrès  7.Classe(prof)
            ┌─────────┬─────────┬──────────┬─────────┬──────────┬─────────┬──────────────┐
🔴 MUST     │ F1+RGPD │  F2     │   F3     │   F4    │   F5     │   F6    │  US-T.1/2/3  │  ← MVP R1
🟠 SHOULD   │ erreurs │ fallback│  RAG/load│   —     │ landing  │ rouvrir │      —       │
🟡 COULD    │ exportG │   —     │ difficulté│   —    │ explic.  │ filtres │ dashboard prof│  ← R2
⚪ WON'T    │ paiement│ LLMcloud│    —     │   —     │ signal.  │ mobile  │      —       │
            └─────────┴─────────┴──────────┴─────────┴──────────┴─────────┴──────────────┘
```

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Commentaire / preuve |
|---|:---:|---|
| Les activités utilisateur (backbone) sont nommées et ordonnées | ☑ Oui | §2 : 7 activités dans l'ordre du parcours, mappées aux epics. |
| Les 4 niveaux MoSCoW sont présents en lignes | ☑ Oui | §3 : MUST / SHOULD / COULD / WON'T. |
| La ligne MUST décrit bien le MVP Release 1 (F1–F6) | ☑ Oui | §3 ligne MUST + §4 walking skeleton. |
| Chaque cellule est tracée vers une user story | ☑ Oui | Renvois US-Fx.x / US-T.x / US-Rx.x du [Product Backlog](product-backlog.md). |
| L'état réel du code (brownfield) est indiqué | ☑ Oui | Icônes ✅/🔧/⬜ par cellule (spécificité équipe 6). |
| Les tranches de livraison (R1/R2/R3) sont identifiées | ☑ Oui | §4 release slices avec échéances. |
| La perturbation J1 (enseignant) est intégrée | ☑ Oui | Colonne 7 « Piloter sa classe » + US-T.x en MUST. |
| La perturbation J4 est intégrée | ☑ Oui | §4bis : activité transverse plateforme publique + E14/E15/E16. |
| Le document a été relu et validé par l'équipe | ☑ Oui | Revue d'équipe avant remise · validation PO en attente. |

---

## 📚 Références

- Jeff Patton — *User Story Mapping* (O'Reilly) : https://www.jpattonassociates.com/story-mapping/
- Cours Agile/Scrum (Mohamed EL AFRIT) — mohamedelafrit.com/teaching/APOCALIPSSI
- Sources internes : [Product Backlog](product-backlog.md) · [Customer Journey Map](03_customer_journey_map.md) · [Personas](personas.md)

---

## 🔄 Convention de versionnement

- **v1.0** — story map initiale issue du cadrage (30/06/2026)
- **v1.x** — recalibrage après revue de sprint / mise à jour de l'état du code
- **v2.0** — révision majeure suite à une perturbation (changement de scope)

---

*Story Map réalisée selon la méthode Jeff Patton — carte 2D activités × MoSCoW, tracée sur le Product Backlog de l'équipe 6.*
*Dépôt : `/docs/cadrage/story-map.md` — v1.0 — 30/06/2026*
