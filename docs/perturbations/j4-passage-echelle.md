# Perturbation J4 — Passage à l'échelle (RGAA · i18n · scalabilité)

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Sprint 6 (jeudi 09h–13h) → Release 2 |
| **Artefact** | Perturbation J4 — Analyse de risques + actions préventives + pilotage |
| **Version** | v1.0 |
| **Date** | 02/07/2026 |
| **Statut** | ✅ Analyse produite (matrice ≥ 5 risques + actions préventives estimées) |
| **Rédacteur** | Hugo RAGUIN |

> Liens : [Burndown & Burnup](../cadrage/j4-burndown-burnup.md) · [Product Backlog](../cadrage/product-backlog.md) · [Release Planning](../cadrage/release-planning.md).
> Source : énoncé du cours — <https://mohamedelafrit.com/teaching/APOCALIPSSI/pages/perturbations/j4-livraison.php>

---

## 1. Scénario

EduTutor IA connaît un **succès viral national** après un passage TV : les serveurs ont **failli s'effondrer**. L'État propose d'en faire la **plateforme officielle des lycées**, à une **condition non négociable : la conformité RGAA (accessibilité)**. En parallèle, une **levée de fonds** finance l'**internationalisation** et la **migration vers une architecture scalable**. Consigne du sponsor : *« pas de code bricolé dans la panique, je veux un plan clair »*.

Trois axes structurants s'imposent donc au produit :

1. **Accessibilité RGAA** — service public = utilisable par tous, y compris en situation de handicap.
2. **Internationalisation (i18n)** — interface multilingue **et** réponses IA multilingues.
3. **Scalabilité** — encaisser des **millions d'utilisateurs simultanés**.

> Reformulation (1 phrase) : *« Transformer un MVP viral en plateforme publique nationale : conforme RGAA, multilingue et scalable — par un plan maîtrisé, pas dans l'urgence. »*

---

## 2. Impact sur les artefacts (les 3 axes) *(CA-J4-1)*

| Artefact | Évolution J4 |
|---|---|
| **Vision board** | La cible passe de « étudiants + enseignants FR » à **service public national multilingue et accessible** ; proposition de valeur : « réviser pour **tous**, partout ». |
| **Personas** | Ajout d'un persona **international / en situation de handicap** (voir §2.1). |
| **Story map** | Nouvelle colonne « Accessibilité & International » ; backbone étendu (choix de langue, navigation clavier). |
| **Product backlog** | 3 nouveaux épics **E14 Scalabilité · E15 Accessibilité (RGAA) · E16 i18n** + US préventives (§4). |
| **Release planning** | Les 3 axes forment une **Release 3 « Plateforme publique »** ; le MVP (R1) et R2 restent livrés. |
| **Next sprint backlog** | Amorce : audit RGAA + ADR migration scalable + i18n de l'interface. |

### 2.1 Nouveau persona (extrait)

> **Amina, 17 ans, lycéenne malvoyante à Marseille (utilise un lecteur d'écran)** — *« Je veux réviser comme les autres : que l'appli soit lisible au clavier et annoncée correctement par NVDA. »* Besoins : navigation **100 % clavier**, contrastes AA, libellés ARIA, pas de piège au focus.
>
> **Variante internationale — Diego, 16 ans, lycéen à Madrid** — *« Je veux l'interface et des quiz en espagnol. »* Besoins : **i18n** de l'UI + **réponses IA en espagnol**.

---

## 3. Analyse de risques — matrice probabilité × impact *(CA-J4-2)*

Échelle : Probabilité **P** (1 faible → 3 élevée) · Impact **I** (1 mineur → 3 critique) · **Score = P × I** (priorité si ≥ 6).

| # | Risque | Axe | P | I | Score | Action préventive (→ backlog) |
|:--:|---|---|:--:|:--:|:--:|---|
| **R1** | Effondrement sous la charge (millions d'users simultanés) | Scalabilité | 3 | 3 | **9 🔴** | File de génération **asynchrone** + workers + autoscaling → **US-SC.1** |
| **R2** | Le LLM **local** (Ollama) ne tient pas la charge nationale | Scalabilité | 3 | 3 | **9 🔴** | Pool GPU + **repli modèle managé UE** en débordement (feature-flag) → **US-SC.2** |
| **R3** | **Non-conformité RGAA** → blocage du marché public (condition non négociable) | Accessibilité | 2 | 3 | **6 🟠** | Audit RGAA + corrections prioritaires (contraste, clavier, ARIA) → **US-A11Y.1** |
| **R4** | Réponses IA multilingues de **qualité inégale** | i18n | 2 | 2 | 4 🟡 | Détection de langue + **prompts localisés** + tests par langue → **US-I18N.2** |
| **R5** | **RGPD à l'international** : transferts / hébergement hors UE | Conformité | 2 | 3 | **6 🟠** | Hébergement **UE** + DPA + registre → **US-RGPD-INT.1** (cf. [rétention](j3bis-politique-retention.md)) |
| **R6** | **Dette technique** (« code bricolé dans la panique ») | Transverse | 2 | 2 | 4 🟡 | Décisions tracées (**ADR migration**) + revue + CI bloquante → **US-SC.3** |
| **R7** | **Explosion des coûts infra** malgré la levée | FinOps | 2 | 2 | 4 🟡 | Quotas + cache + observabilité coûts (FinOps) → **US-SC.4** |

> **Risques prioritaires (score ≥ 6)** : R1, R2, R3, R5 → chacun a **au moins une action préventive estimée** au backlog (§4). *(CA-J4-3)*

---

## 4. Actions préventives estimées (→ Product Backlog) *(CA-J4-3)*

Nouveaux épics : **E14 Scalabilité · E15 Accessibilité · E16 i18n**. Estimation en points (Fibonacci).

| US | Épic | Intitulé | Risque couvert | MoSCoW | Est. |
|---|---|---|:--:|:--:|:--:|
| **US-SC.1** | E14 | Génération de quiz **asynchrone** (file + workers) | R1 | 🔴 M | 13 |
| **US-SC.2** | E14 | **Repli LLM managé UE** en débordement (feature-flag) | R2 | 🔴 M | 8 |
| **US-SC.3** | E14 | **ADR de migration** scalable + cache/CDN + autoscaling | R1/R6 | 🟠 S | 8 |
| **US-SC.4** | E14 | Observabilité & **FinOps** (quotas, métriques coûts) | R7 | 🟢 C | 5 |
| **US-A11Y.1** | E15 | **Audit RGAA** + corrections prioritaires (contraste, clavier, ARIA) | R3 | 🔴 M | 8 |
| **US-A11Y.2** | E15 | Tests d'**accessibilité automatisés** (axe-core en CI) | R3 | 🟠 S | 5 |
| **US-I18N.1** | E16 | **i18n de l'interface** (FR/EN, extensible) | i18n | 🟠 S | 8 |
| **US-I18N.2** | E16 | **Réponses IA multilingues** (détection langue + prompts localisés) | R4 | 🟠 S | 8 |
| **US-RGPD-INT.1** | E8 | **Hébergement UE + DPA** pour l'international | R5 | 🔴 M | 5 |

> Total ≈ **68 points** de scope préventif ajouté (visible dans le [burnup](../cadrage/j4-burndown-burnup.md) comme un saut de périmètre).

---

## 5. Pilotage — burndown & burnup *(CA-J4-4)*

Les courbes (et l'**impact chiffré des perturbations** sur le périmètre) sont dans le document dédié : **[Burndown & Burnup](../cadrage/j4-burndown-burnup.md)**.

- **Burndown** (sprint MVP) : reste-à-faire vs ligne idéale.
- **Burnup** (projet S1→S8) : réalisé vs **périmètre**, avec les **sauts de scope** J1 (+13, espace enseignant), J3/J3-bis (+8, sécurité/RGPD) et **J4 (+68, RGAA/i18n/scalabilité)**.

---

## 6. Critères d'acceptation J4

- [x] **CA-J4-1** — Vision, story map & **personas** intègrent les 3 axes → §2 (+ persona handicap/international)
- [x] **CA-J4-2** — Matrice de risques **≥ 5** (probabilité × impact) → §3 (7 risques)
- [x] **CA-J4-3** — Chaque risque prioritaire → **action préventive estimée au backlog** → §4
- [x] **CA-J4-4** — **Burndown + burnup** actualisés, impact des perturbations chiffré → [doc dédié](../cadrage/j4-burndown-burnup.md)
- [x] **CA-J4-5** — **Historique** des sprints conservé + prochain sprint défini → [Release Planning](../cadrage/release-planning.md)
- [ ] **CA-J4-6** — *Bonus* — PoC technique (ADR migration scalable / amorce i18n)

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Preuve |
|---|:---:|---|
| 3 axes intégrés aux artefacts | ☑ Oui | §2. |
| Persona international / handicap | ☑ Oui | §2.1. |
| Matrice risques ≥ 5 (P × I) | ☑ Oui | §3 (7 risques). |
| Actions préventives estimées au backlog | ☑ Oui | §4 (9 US, épics E14–E16). |
| Impact des perturbations chiffré | ☑ Oui | burnup (+68 pts J4). |
| Historique conservé + prochain sprint | ☑ Oui | release planning. |

---

## 📚 Références

- **RGAA** (accessibilité) — <https://accessibilite.numerique.gouv.fr/> · **WCAG 2.1 AA**
- Sources internes : [Burndown & Burnup](../cadrage/j4-burndown-burnup.md) · [Product Backlog](../cadrage/product-backlog.md) · [Release Planning](../cadrage/release-planning.md) · [Politique de rétention](j3bis-politique-retention.md).

---

*Perturbation J4 — passage à l'échelle de l'équipe 6 : 3 axes (RGAA / i18n / scalabilité), matrice de 7 risques, 9 actions préventives estimées, pilotage burndown/burnup.*
