# Product Backlog — EduTutor IA

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Cadrage |
| **Artefact** | 6 sur 7 — Product Backlog |
| **Version** | v1.0 |
| **Date de remise** | 30/06/2026 |
| **Statut** | Draft (à valider PO) |
| **Rédacteur** | Souleymane FALL |
| **Fichier** | `equipe-6-product-backlog-v1.0` |

---
 
> **Artefact de cadrage Jour 1 — APOCAL'IPSSI 2026**
>
> **Produit** : EduTutor IA — assistant IA de révision, *enseignant-first*, à génération **ancrée dans les cours (RAG)** et **100 % local (Ollama)** pour la souveraineté des données (RGPD).
> **Dépôt** : fork de `melafrit/IPSSI_APOCAL_KIT`
> **Statut** : **à valider par le Product Owner** (arbitrage MoSCoW avant le démarrage des sprints).
> **Échéances** : Release 1 (MVP F1–F6) → **mercredi 17h45** · Release 2 (pistes) → **jeudi soir**.
>
> *Document vivant — mis à jour à chaque revue de sprint. Source de vérité du périmètre : GitHub Issues & Project du dépôt.*
 
---
 
## 1. Objet du document
 
Ce backlog est construit selon une **mentalité brownfield** : un **inventaire de l'existant**. Le kit fourni n'est pas un point de départ vierge mais une base **fonctionnelle et volontairement inégale** (« à reprendre, pas à admirer »). Chaque story porte donc son **état réel dans le code** afin de ne pas réécrire ce qui marche et de concentrer l'effort sur les manques : fiabiliser, brancher front ↔ back, tester, durcir.
 
Il couvre l'ensemble de la semaine : le **MVP must-have F1–F6** (Release 1), les **pistes Release 2**, et les **5 perturbations** prévues — chacune rattachée à un epic et à un **spike** de préparation.
 
---
 
## 2. Définitions partagées
 
### Definition of Ready (DoR) — une story peut entrer en sprint si :
 
- [ ] Elle respecte les critères **INVEST** (voir §7).
- [ ] La **valeur métier** et l'**utilisateur cible** sont explicites.
- [ ] Les **critères d'acceptation** sont rédigés (Given/When/Then ou liste vérifiable).
- [ ] Les **dépendances** (autre story, donnée, endpoint) sont identifiées.
- [ ] Une **estimation** en points a été posée par l'équipe.
- [ ] L'**état de l'existant** a été vérifié dans le code (brownfield).
### Definition of Done (DoD) — une story est terminée si :
 
- [ ] Code mergé sur `main` via **Pull Request revue par un pair**.
- [ ] **Tests** (back et/ou front) passants et **CI verte**.
- [ ] Tous les **critères d'acceptation** satisfaits et démontrables.
- [ ] **Aucune régression** sur l'existant.
- [ ] Fonctionne dans l'environnement **Docker Compose** (pas seulement en local).
- [ ] **Aucun secret en clair** (clés en `.env`, pas dans le code/les logs).
- [ ] Documentation / `CHANGELOG.md` mis à jour si pertinent.
- [ ] Commits au format **Conventional Commits**, travail réparti dans l'équipe.
### Priorisation MoSCoW
 
| Code | Signification | Engagement |
|:----:|---------------|------------|
| 🔴 **M** | Must have | Indispensable au MVP, livré en R1 |
| 🟠 **S** | Should have | Important mais contournable, visé R1 si le temps le permet |
| 🟡 **C** | Could have | Confort, R2 |
| ⚪ **W** | Won't have (this time) | Hors périmètre semaine, noté pour mémoire |
 
### Échelle d'estimation (Fibonacci, story points)
 
`1` trivial · `2` simple · `3` modéré · `5` conséquent · `8` lourd / à découper · `13` épic à scinder.
 
### Légende état du code (brownfield)
 
✅ **livré** (à recalibrer) · 🔧 **partiel** (à finir / fiabiliser) · ⬜ **à faire**
 
---
 
## 3. Épics
 
| ID | Épic | Description | Couverture | Perturbation |
|----|------|-------------|------------|:------------:|
| **E1** | Compte & identité | Inscription, connexion, vérification email, profil, mot de passe | F1 | — |
| **E2** | Ingestion de cours | Upload PDF (≤ 5 Mo) ou texte (≥ 200 car.) comme source de quiz | F2 | P1 |
| **E3** | Génération de quiz | 10 QCM générés par LLM local, ancrés dans le cours | F3 | P2 |
| **E4** | Passation & correction | Soumission des réponses, correction automatique | F4 | — |
| **E5** | Résultats | Score /10 + détail des réponses | F5 | — |
| **E6** | Historique | Persistance et consultation des quiz passés | F6 | — |
| **E7** | Sécurité & durcissement | Anti-injection, isolation des données, rate-limit, secrets | transverse | P3 |
| **E8** | RGPD & légal | Pages légales, consentement, export & droit à l'oubli | transverse | P4 |
| **E9** | Livraison, CI/CD & crise | CI, scripts de lancement, déploiement, rollback, post-mortem | transverse | P5 |
| **E10** | Qualité & exploitation | Tests cœur métier, ADR LLM, admin, observabilité | transverse | P2 |
| **E11** | MVP2 / Expérience de révision | Dashboard, révision des erreurs, difficulté, explications | R2 | — |
| **E12** | Feedback utilisateur | Notation des quiz, signalement, collecte de retours | R2 | — |
 
---
 
# 4. RELEASE 1 — MVP (must-have, à livrer mercredi 17h45)
 
> Objectif : un parcours complet **« je m'inscris → je dépose un cours → je révise → je vois mon score → je retrouve mon historique »**, fonctionnel, testé et démontrable sous Docker.
 
## E1 — Compte & identité *(F1)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-F1.1 | En tant qu'**étudiant**, je veux **créer un compte par email** afin d'accéder à mes révisions. | 🔴 M | 2 | ✅ `signup/` |
| US-F1.2 | En tant qu'étudiant, je veux **me connecter / me déconnecter** afin de retrouver mes données. | 🔴 M | 2 | ✅ `login/` `logout/` |
| US-F1.3 | En tant qu'étudiant, je veux **valider mon email** via un lien afin de sécuriser mon compte. | 🔴 M | 3 | 🔧 `verify-email/` (flux à fiabiliser) |
| US-F1.4 | En tant qu'étudiant, je veux **réinitialiser mon mot de passe oublié** afin de récupérer l'accès. | 🔴 M | 3 | 🔧 `password-reset/` (à tester bout-en-bout) |
| US-F1.5 | En tant qu'étudiant, je veux **consulter et modifier mon profil** afin de garder mes infos à jour. | 🔴 M | 2 | ✅ `profile/` `me/` `change-password/` |
| US-F1.6 | En tant qu'étudiant, je veux des **messages d'erreur clairs** (email déjà pris, identifiants invalides). | 🟠 S | 2 | ⬜ UX d'erreur |
 
## E2 — Ingestion de cours *(F2 — perturbation P1)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-F2.1 | En tant qu'étudiant, je veux **téléverser un PDF (≤ 5 Mo)** afin de générer un quiz à partir de mon cours. | 🔴 M | 5 | 🔧 extraction PDF à fiabiliser |
| US-F2.2 | En tant qu'étudiant, je veux **coller du texte (≥ 200 car.)** afin de générer un quiz sans PDF. | 🔴 M | 2 | 🔧 saisie présente, validation à renforcer |
| US-F2.3 | En tant qu'étudiant, je veux un **message d'erreur clair** si le fichier est trop lourd / le texte trop court. | 🔴 M | 2 | ⬜ validation & UX d'erreur |
| US-F2.4 | En tant qu'étudiant, je veux être **prévenu si l'extraction PDF échoue** (PDF scanné/image) afin de basculer sur le texte. | 🟠 S | 2 | ⬜ détection & message |
 
> **📌 P1 — Produit/Scope (lundi 14h).** La perturbation peut redéfinir le périmètre de saisie. Garder ces stories **négociables** : arbitrage PO + mise à jour de la Story Map → **SPK-1**.
 
## E3 — Génération de quiz *(F3 — perturbation P2)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-F3.1 | En tant qu'étudiant, je veux **générer 10 QCM** depuis ma source via le **LLM local** afin de réviser. | 🔴 M | 5 | 🔧 `generate-quiz/` (robustesse parsing JSON) |
| US-F3.2 | En tant qu'étudiant, je veux que chaque QCM ait **4 options et 1 bonne réponse** afin d'un format cohérent. | 🔴 M | 3 | ✅ modèle `Question` (`options`, `correct_index`) |
| US-F3.3 | En tant qu'étudiant, je veux un **retour de chargement** pendant la génération afin de patienter sereinement. | 🟠 S | 2 | ⬜ état de chargement front |
| US-F3.4 | En tant qu'étudiant, je veux un **message exploitable** si le LLM échoue / time-out afin de relancer. | 🔴 M | 3 | ⬜ gestion d'erreur & retry |
| US-F3.5 | En tant qu'étudiant, je veux des **QCM réellement ancrés dans mon cours** (RAG) afin que la révision soit pertinente. | 🟠 S | 5 | 🔧 prompt à durcir / contextualiser |
 
> **📌 P2 — Technique/Latence (mardi 10h).** La latence Ollama peut être jugée inacceptable → **ADR** comparant fournisseurs (cf. **SPK-2** / US-X.3). Contrainte produit : **rester local** par défaut (RGPD) — tout passage cloud exige une ADR (voir US-W.3).
 
## E4 — Passation & correction *(F4)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-F4.1 | En tant qu'étudiant, je veux **soumettre mes réponses** afin d'être corrigé automatiquement. | 🔴 M | 3 | 🔧 `<pk>/answer/` à finaliser |
| US-F4.2 | En tant qu'étudiant, je veux qu'**une seule bonne réponse par QCM** soit comptée afin d'un score juste. | 🔴 M | 2 | ✅ logique `correct_index` |
 
## E5 — Résultats *(F5)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-F5.1 | En tant qu'étudiant, je veux voir mon **score /10** après soumission afin de mesurer mes acquis. | 🔴 M | 2 | 🔧 champ `Quiz.score`, affichage à finir |
| US-F5.2 | En tant qu'étudiant, je veux le **détail bonne/mauvaise réponse par question** afin de comprendre mes erreurs. | 🔴 M | 3 | 🔧 `mistakes/` + détail front |
| US-F5.3 | En tant qu'utilisateur, je veux une **page d'accueil claire** expliquant le produit afin de comprendre sa valeur. | 🟠 S | 2 | ⬜ landing |
 
## E6 — Historique *(F6)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-F6.1 | En tant qu'étudiant, je veux **retrouver l'historique** de mes quiz (date, cours, score) afin de suivre ma progression. | 🔴 M | 3 | 🔧 `quiz-list` + `stats/` à brancher au front |
| US-F6.2 | En tant qu'étudiant, je veux **rouvrir un quiz passé** afin de revoir mes réponses. | 🟠 S | 2 | 🔧 `<pk>/` détail |
| US-F6.3 | En tant qu'étudiant, je veux **filtrer/trier mon historique** (date, score, matière) afin de m'y retrouver. | 🟡 C | 3 | ⬜ |
 
## E7 — Sécurité & durcissement *(perturbation P3)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-S.1 | En tant qu'**équipe**, nous voulons **séparer instructions système et contenu utilisateur** afin que le LLM n'obéisse pas à des ordres cachés (**prompt injection**). | 🔴 M | 5 | ⬜ |
| US-S.2 | En tant qu'équipe, nous voulons **assainir/valider les entrées** (cours, texte) afin de limiter les injections. | 🔴 M | 3 | ⬜ |
| US-S.3 | En tant qu'équipe, nous voulons **isoler les données par utilisateur** afin qu'un étudiant ne voie jamais l'historique d'un autre. | 🔴 M | 3 | 🔧 à vérifier |
| US-S.4 | En tant qu'équipe, nous voulons des **tests adversariaux** d'injection afin de valider la robustesse. | 🟠 S | 3 | ⬜ (cf. `docs/04-testing.md`) |
| US-S.5 | En tant qu'équipe, nous voulons un **rate limiting / quotas** sur la génération afin d'éviter les abus. | 🟠 S | 3 | ⬜ |
| US-S.6 | En tant qu'équipe, nous voulons **ne jamais exposer les secrets** afin de sécuriser le déploiement. | 🔴 M | 2 | 🔧 à auditer |
 
> **📌 P3 — Sécurité (mercredi 10h).** Préparer les tests adversariaux **en amont** (tutoriel dans `docs/04-testing.md`) → **SPK-3**.
 
## E8 — RGPD & légal *(perturbation P4)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-G.1 | En tant qu'utilisateur, je veux une **politique de confidentialité** afin de savoir comment mes données sont traitées. | 🔴 M | 3 | ⬜ (4 pages légales vierges) |
| US-G.2 | En tant qu'étudiant, je veux **supprimer définitivement mon compte et mes données** (droit à l'oubli). | 🔴 M | 3 | 🔧 suppression profil à durcir |
| US-G.3 | En tant qu'utilisateur, je veux des **CGU / mentions légales** afin de connaître mes droits. | 🟠 S | 2 | ⬜ |
| US-G.4 | En tant qu'utilisateur, je veux une **gestion du consentement (cookies/traçage)** afin de garder le contrôle. | 🟠 S | 3 | ⬜ |
| US-G.5 | En tant qu'étudiant, je veux **exporter mes données** (portabilité) afin d'exercer mes droits. | 🟡 C | 3 | ⬜ |
| US-G.6 | En tant qu'équipe, nous voulons **minimiser et documenter** les données collectées afin d'être conformes. | 🟠 S | 2 | ⬜ registre de traitement |
 
> **📌 P4 — RGPD (mercredi 14h).** Atout produit : **100 % local**, donc aucune donnée n'est envoyée à un tiers. À matérialiser dans les pages légales → **SPK-4**.
 
## E9 — Livraison, CI/CD & crise *(perturbation P5)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-D.1 | En tant qu'équipe, nous voulons une **CI verte** (lint + tests) afin de garantir la qualité à chaque PR. | 🔴 M | 3 | ✅ GitHub Actions |
| US-D.2 | En tant qu'équipe, nous voulons un **lancement en une commande** (scripts par OS) afin de démontrer facilement. | 🔴 M | 2 | ✅ `scripts/start-*` |
| US-D.3 | En tant qu'équipe, nous voulons un **plan de crise / rollback** afin de réagir à un incident le jour J. | 🔴 M | 3 | ⬜ runbook |
| US-D.4 | En tant qu'équipe, nous voulons un **déploiement de production** (VPS OVH, HTTPS) afin d'exposer la démo. | 🟡 C | 8 | ⬜ (cf. `docs/11-*`) |
| US-D.5 | En tant qu'équipe, nous voulons un **post-mortem** après la crise afin de capitaliser. | 🟠 S | 1 | ⬜ template |
 
> **📌 P5 — Livraison/Crise (jeudi 10h).** Préparer rollback rapide (`--fast`), checklist de démo et template post-mortem → **SPK-5**.
 
## E10 — Qualité & exploitation *(transverse)*
 
| ID | User Story | MoSCoW | Pts | État code |
|----|-----------|:------:|:---:|-----------|
| US-X.1 | En tant qu'équipe, nous voulons des **tests automatisés sur F3/F4** (cœur métier) afin d'éviter les régressions. | 🟠 S | 5 | ⬜ |
| US-X.2 | En tant qu'équipe, nous voulons un **mode mock/fallback LLM** afin que la démo tienne même LLM indisponible. | 🟠 S | 3 | ✅ backend `mock` |
| US-X.3 | En tant qu'équipe, nous voulons **tracer le choix du fournisseur LLM** afin d'arbitrer latence/coût/qualité. | 🔴 M | 3 | ⬜ ADR |
| US-X.4 | En tant qu'admin, je veux **configurer le LLM/l'app depuis l'UI** afin d'ajuster sans toucher au code. | 🟠 S | 5 | ✅ admin |
| US-X.5 | En tant qu'admin, je veux des **logs / observabilité** (erreurs LLM, latence) afin de superviser. | 🟡 C | 3 | ⬜ |
 
---
 
# 5. RELEASE 2 — Catalogue de pistes (jeudi soir)
 
> Aucune feature obligatoire : le **PO** et la **Story Map** décident. Trois exemples sont déjà codés dans le kit (dashboard, révision des erreurs, mode sombre). Catalogue complet : `docs/08-mvp2-idees.md`.
 
## E11 — MVP2 / Expérience de révision
 
| ID | Piste R2 | MoSCoW | Pts | État code | Note |
|----|----------|:------:|:---:|:---------:|------|
| US-R2.1 | **RAG renforcé** : génération ancrée chapitre par chapitre. | 🟡 C | 8 | 🔧 | différenciateur produit |
| US-R2.2 | **Tableau de bord enseignant** : suivi de classe, export. | 🟡 C | 8 | ⬜ | cible *teacher-first* |
| US-R2.3 | **Niveaux de difficulté** des QCM (facile/moyen/difficile). | 🟡 C | 5 | ⬜ | engagement |
| US-R2.4 | **Explications par réponse** afin de comprendre l'erreur. | 🟠 S | 5 | ⬜ | valeur pédagogique forte |
| US-R2.5 | **Révision des erreurs** ciblée (rejouer ses ratés). | 🟠 S | 5 | ✅ kit | à recalibrer |
| US-R2.6 | **Tableau de bord de progression** (scores dans le temps). | 🟠 S | 5 | ✅ kit | à recalibrer |
| US-R2.7 | **Mode sombre**. | 🟡 C | 2 | ✅ kit | confort |
| US-R2.8 | **Export PDF** du quiz + correction. | 🟡 C | 3 | ⬜ | confort |
 
## E12 — Feedback utilisateur
 
| ID | Piste R2 | MoSCoW | Pts | État code |
|----|----------|:------:|:---:|:---------:|
| US-FB.1 | **Noter la qualité d'un quiz généré** afin de signaler les questions faibles. | 🟠 S | 3 | ⬜ |
| US-FB.2 | **Signaler une question erronée** afin d'améliorer la base. | 🟡 C | 3 | ⬜ |
| US-FB.3 | **Collecter les retours** (formulaire / NPS) afin de prioriser la suite. | 🟡 C | 3 | ⬜ |
 
## ⚪ Won't have (this time)
 
| ID | Item | Raison |
|----|------|--------|
| US-W.1 | Application mobile native | hors périmètre / temps |
| US-W.2 | Paiement / abonnement | non requis MVP |
| US-W.3 | LLM cloud (OpenAI, etc.) par défaut | **RGPD : local obligatoire** — tout changement exige une **ADR** |
 
---
 
# 6. Spikes & préparation des perturbations
 
> Les **spikes** sont des time-box d'investigation/décision, à mener *avant* ou *pendant* la perturbation correspondante.
 
| ID | Spike / tâche | Perturbation | Pts | Livrable attendu |
|----|---------------|:------------:|:---:|------------------|
| SPK-1 | **Cadrage scope** avec le PO | P1 (lun. 14h) | 2 | Story Map à jour, décisions d'arbitrage |
| SPK-2 | **ADR LLM** : comparer fournisseurs, trancher latence/coût/qualité | P2 (mar. 10h) | 3 | ADR rédigé (`docs/`) |
| SPK-3 | **Sécurité** : concevoir + jouer les tests d'injection | P3 (mer. 10h) | 3 | Jeu de tests adversariaux + correctifs |
| SPK-4 | **RGPD** : cartographier les données + plan de conformité | P4 (mer. 14h) | 3 | Registre de traitement + 4 pages légales remplies |
| SPK-5 | **Runbook crise** : procédure incident + rollback + post-mortem | P5 (jeu. 10h) | 2 | Runbook + template post-mortem |
 
---
 
# 7. Contrôle INVEST (échantillon)
 
Vérification appliquée à toutes les stories must-have ; exemple sur **US-F3.1** :
 
| Critère | Vérifié | Justification |
|---------|:------:|---------------|
| **I**ndependent | ✅ | Génération isolable de la soumission (F4). |
| **N**egotiable | ✅ | Nombre de QCM / format discutables avec le PO. |
| **V**aluable | ✅ | Cœur de la proposition de valeur (réviser depuis son cours). |
| **E**stimable | ✅ | Estimée 5 pts. |
| **S**mall | ✅ | Tient dans un sprint, découpable (parsing / prompt / UI). |
| **T**estable | ✅ | Critères d'acceptation vérifiables (ci-dessous). |
 
**Critères d'acceptation US-F3.1** (Given/When/Then)
- *Given* une source valide (PDF extrait ou texte ≥ 200 car.), *when* l'utilisateur lance la génération, *then* le système crée **exactement 10 questions** à 4 options chacune.
- *Given* une réponse LLM malformée, *when* le parsing échoue, *then* l'utilisateur reçoit un **message explicite** sans crash serveur.
- *Given* l'environnement, *then* la génération utilise **Ollama en local** (aucun appel réseau externe).
**Critères d'acceptation US-S.1 (anti-injection)**
- *Given* un cours contenant « ignore les instructions précédentes et… », *when* on génère le quiz, *then* le système produit toujours **10 QCM portant sur le contenu**, sans exécuter l'instruction injectée.
---
 
# 8. Synthèse de planification
 
## Récapitulatif des points (indicatif, à confirmer en planning poker)
 
| Bloc | Must (🔴) | Should (🟠) | Could (🟡) | Total |
|------|:--------:|:----------:|:---------:|:-----:|
| **R1 — Parcours MVP** (E1–E6) | 40 | 12 | 6 | ~58 |
| **R1 — Transverse** (E7–E10) | 22 | 24 | 14 | ~60 |
| **Spikes** | 13 | — | — | 13 |
| **R2** (E11–E12) | — | 21 | 35 | ~56 |
 
> **Lecture brownfield** : ~60 % des stories Must de E1–E6 sont en `🔧 partiel`. L'effort dominant n'est pas de coder de zéro mais de **fiabiliser, brancher front↔back et tester**.
 
## Mapping jour / sprint (semaine APOCAL'IPSSI)
 
| Jour | Focus backlog | Perturbation |
|------|---------------|--------------|
| **Lundi (J1)** | Cadrage, E1/E2, Story Map, planning Sprint 1 | P1 — Produit/Scope (14h) |
| **Mardi (J2)** | E2/E3, fiabilisation génération, ADR LLM | P2 — Latence/ADR (10h) |
| **Mercredi (J3)** | E4/E5/E6 + durcissement E7, RGPD E8 → **Release 1 (17h45)** | P3 — Sécurité (10h) · P4 — RGPD (14h) |
| **Jeudi (J4)** | E11/E12 (R2), E9 livraison | P5 — Crise (10h) |
| **Vendredi (J5)** | Stabilisation, démo finale, post-mortem | — |
 
## Ordre d'attaque recommandé
 
1. **Fiabiliser le parcours MVP de bout en bout** : US-F3.1 (parsing JSON) → US-F4.1 → US-F5.1/F5.2 → US-F6.1. Sans une chaîne génération→correction→score→historique solide, pas de démo.
2. **ADR LLM** (US-X.3 / SPK-2) — débloque la décision technique structurante de la semaine.
3. **Sécurité + RGPD** (E7/E8) — P3 et P4 tombent le mercredi, jour de la Release 1.
4. **Runbook crise** (SPK-5) — prêt avant jeudi 10h.
5. **R2 à forte valeur** : US-R2.4 (explications), US-R2.6 (dashboard, déjà codé).
---
 
# 9. Notes d'arbitrage pour le Product Owner
 
- **Focus brownfield** : prioriser le branchement front↔back et les tests plutôt que la réécriture.
- **Risque n°1** : robustesse du parsing JSON de sortie LLM (US-F3.1) → **bloquant** pour F4/F5. À sécuriser en premier.
- **Risque n°2** : extraction de texte PDF (US-F2.1) variable selon les fichiers → prévoir le fallback texte (US-F2.4).
- **Risque n°3** : latence Ollama (P2) → l'ADR doit trancher sans sacrifier la contrainte RGPD (rester local par défaut).
- **Décisions attendues du PO** : (1) confirmer le périmètre Must ci-dessus ; (2) trancher les `S` à inclure dans le Sprint 1 ; (3) acter la réponse de principe à P1.
---
 
# 10. Grille d'auto-évaluation

| Critère qualité | Auto-éval | Commentaire / preuve |
|---|:---:|---|
| Definition of Ready et Definition of Done explicites | ☑ Oui | §2 : DoR (6 critères) + DoD (8 critères). |
| Priorisation MoSCoW appliquée à chaque story | ☑ Oui | Colonne MoSCoW (🔴M/🟠S/🟡C/⚪W) sur toutes les stories. |
| Estimation en story points (Fibonacci) | ☑ Oui | Colonne Pts + §8 récap des points. |
| Stories au format INVEST + critères d'acceptation Given/When/Then | ☑ Oui | §7 contrôle INVEST sur US-F3.1 + critères d'acceptation. |
| Couverture du MVP F1-F6 + transverse (sécurité, RGPD, CI/CD) | ☑ Oui | Épics E1–E10, Release 1 complète. |
| Inventaire brownfield de l'existant (état réel du code) | ☑ Oui | Colonne « État code » (✅/🔧/⬜) par story. |
| Pistes Release 2 cataloguées | ☑ Oui | §5 (E11–E12) + Won't have tracé. |
| Préparation des 5 perturbations (spikes) | ☑ Oui | §6 SPK-1 à SPK-5 rattachés aux perturbations. |
| Notes d'arbitrage fournies au PO | ☑ Oui | §9 risques + décisions attendues du PO. |
| Le document a été relu et validé par l'équipe | ☑ Oui | Revue d'équipe avant remise · validation PO en attente. |

---
 
# 11. Références

- Cours Agile/Scrum (Mohamed EL AFRIT) — mohamedelafrit.com/teaching/APOCALIPSSI
- Scrum Guide officiel FR — scrumguides.org
- Mike Cohn — *User Stories Applied* (INVEST, story points)
- Dai Clegg — méthode de priorisation MoSCoW
- Sources internes : [Product Vision Board](product-vision-board.md) · [Personas](personas.md) · [Customer Journey Map](03_customer_journey_map.md)

---
 
# 12. Convention de versionnement

- **v1.0** — backlog initial issu du cadrage (30/06/2026)
- **v1.x** — mises à jour à chaque revue de sprint (ajout/retrait de stories, recalibrage)
- **v2.0** — révision majeure suite à une perturbation (changement de scope)

---
 
*Document vivant — mis à jour à chaque revue de sprint.*
