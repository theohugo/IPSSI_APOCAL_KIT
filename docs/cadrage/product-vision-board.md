# Product Vision Board — EduTutor IA

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Cadrage |
| **Artefact** | 1 sur 7 — Product Vision Board |
| **Version** | v1.0 |
| **Date de remise** | 29/06/2026 |
| **Statut** | Draft (à valider PO) |
| **Rédacteur** | Dina CHAOUKI |
| **Fichier** | `equipe-6-product-vision-board-v1.0` |
| **Méthode** | Roman Pichler (5 composants) + Vision Statement Geoffrey Moore |

---

## 🌟 Vision Statement

> *Formule Geoffrey Moore — Crossing the Chasm*

**Pour** les étudiant·e·s du supérieur qui peinent à réviser efficacement à partir de leurs cours et documents,  
**EduTutor IA** est une application web pédagogique  
**qui** génère automatiquement des quiz personnalisés (QCM) à partir des propres supports de l'utilisateur (PDF ou texte libre) via une IA locale souveraine.  
**Contrairement à** Quizlet AI, Wilgo ou Khanmigo qui produisent des résumés génériques à partir de contenus tiers,  
**notre produit** ancre chaque question directement dans le document fourni par l'enseignant, garantit une conformité RGPD totale (aucune donnée hors UE) et offre une traçabilité pédagogique vérifiable question par question.

---

## 👥 Target Groups (Groupes cibles)

> Trois niveaux de cibles : **primaire** (acteurs principaux du MVP), **secondaire/tertiaire** (acheteur B2B), avec **volume marché FR** et **critère de décision** pour chacune.

| Segment | Profil & volume marché (FR) | Pain point | Critère de décision |
|---|---|---|---|
| **Étudiant·e du supérieur** *(cible primaire)* | 18-28 ans, BTS / Licence / Master · usage smartphone & laptop quotidien · **~2,7 M d'étudiant·e·s dans le supérieur** (MESR 2024) | 5 à 15 h/semaine perdues à chercher ou créer des supports de révision | Confidentialité des cours (local-first) + génération rapide (< 60 s) |
| **Enseignant·e** *(cible primaire — décision PO J1)* | Ex. Mme Sophie Lefèvre, 42 ans, prof de BTS Communication à Lyon, 28 étudiants · maîtrise numérique modérée · **~770 000 enseignant·e·s** (Éducation nationale 2024) | ~12 h/mois en correction et préparation de supports d'évaluation ; aucune vue d'ensemble des décrocheurs | Interface simple sans configuration + suivi de classe + conformité RGPD des données élèves |
| **Établissement scolaire** *(cible tertiaire — acheteur B2B)* | Direction de lycée privé / BTS / école supérieure · responsable pédagogique ou DSI · **~7 500 lycées + ~3 500 établissements du supérieur** | Budget edtech contraint (< 5 €/élève/an) + obligation RGPD non négociable | Aucune donnée hors UE (clause contractuelle) + coût prévisible par élève/an |
| **Administrateur plateforme** *(interne)* | Équipe EduTutor. Gère la configuration du LLM, les utilisateurs, la modération et les KPIs produit. | Maintien en condition opérationnelle du service et de la souveraineté | Contrôle total de la stack (Ollama local) sans dépendance cloud |

> **Note de cadrage (perturbation J1).** Le Product Owner a repositionné l'enseignant·e **cible primaire au même niveau que l'étudiant** : les fonctionnalités de suivi de classe entrent dans le périmètre prioritaire (voir [Personas](personas.md) et [Perturbation J1](perturbations/j1-produit.md)). L'**établissement** reste cible tertiaire (acheteur B2B), pertinente pour le modèle économique mais hors périmètre MVP.

---

## 💡 Needs — Besoins par groupe cible

### Étudiant·e (cible primaire)
- « En tant qu'étudiant·e, j'ai besoin de **générer un quiz depuis mon cours en PDF** pour tester mes connaissances sans effort de création. »
- « En tant qu'étudiant·e, j'ai besoin de **voir mes erreurs détaillées après chaque quiz** pour savoir précisément ce que je n'ai pas compris. »
- « En tant qu'étudiant·e, j'ai besoin d'**un historique de mes scores** pour mesurer ma progression dans le temps. »

### Enseignant·e — Mme Lefèvre *(cible primaire — perturbation J1)*
- « En tant qu'enseignant·e, j'ai besoin de **visualiser les scores de mes 28 étudiants** pour identifier ceux qui décrochent avant l'examen. »
- « En tant qu'enseignant·e, j'ai besoin de **repérer les décrocheurs en 3 clics** (tri/alerte sur scores faibles) pour intervenir rapidement. »
- « En tant qu'enseignant·e, j'ai besoin d'**envoyer des conseils ciblés** à un étudiant en difficulté sans quitter l'outil. »

### Administrateur
- « En tant qu'administrateur, j'ai besoin de **configurer le fournisseur LLM** (Ollama local par défaut) pour garantir la souveraineté des données. »
- « En tant qu'administrateur, j'ai besoin de **gérer les comptes utilisateurs** (création, suspension, suppression) pour assurer la qualité du service. »

---

## 📦 Product — Fonctionnalités clés (must-have Release 1)

> Niveau stratégique uniquement — les détails sont dans le Product Backlog.

| # | Fonctionnalité | Valeur |
|---|---|---|
| F1 | **Auth complète par email** : inscription, validation par lien, connexion, reset mot de passe, page profil | Sécurité & confiance |
| F2 | **Saisie de cours** : upload PDF ≤ 5 Mo ou texte ≥ 200 caractères | Ancrage pédagogique |
| F3 | **Génération automatique de 10 QCM** via LLM local (Ollama — Llama 3.1 8B ou Phi-3-mini) | Différenciateur IA souveraine |
| F4 | **Soumission & correction automatique** : 1 bonne réponse par QCM | Apprentissage actif |
| F5 | **Score /10 + détail bonnes/mauvaises réponses** | Feedback immédiat |
| F6 | **Historique persisté des quiz** par utilisateur (date, cours, score) | Suivi de progression |

---

## 📊 Business Goals — Objectifs mesurables (SMART)

| Objectif | Métrique | Horizon |
|---|---|---|
| **Adoption** | 500 étudiant·e·s inscrit·e·s | 6 mois après launch |
| **Engagement** | Taux de rétention ≥ 60 % | À 3 mois |
| **Satisfaction** | Score moyen ≥ 4/5 sur les quiz générés | Continu dès MVP |
| **Souveraineté** | 0 donnée utilisateur hors UE (RGPD) | Dès le 1er jour |
| **Bouche-à-oreille** | NPS (Net Promoter Score) ≥ 40 | À 6 mois |
| **B2B éducation** | 10 établissements partenaires pilotes | 12 mois |

---

## 🆚 Positionnement concurrentiel

| Concurrent | Point fort | Faiblesse vs EduTutor |
|---|---|---|
| Wilgo | Compagnon IA FR pour étudiants | Contenu générique, pas ancré dans le cours de l'étudiant |
| Quizlet AI | Base utilisateurs massive | OpenAI → données hors UE, non RGPD |
| Khanmigo | Tuteur interactif Khan Academy | Cible US, pas de souveraineté des données FR |
| Leo | Ancré programme officiel FR | Pas d'upload de cours personnels |

**Avantage différenciant EduTutor IA :**  
1. Prompts métier enseignant-first (pas étudiant-first)  
2. Ancrage dans le document fourni → pas d'hallucination non traçable  
3. Ollama local → 100 % RGPD, prérequis contractuel B2B éducation FR

---

## 📐 Contraintes techniques imposées

| Contrainte | Valeur |
|---|---|
| Stack back | Django + DRF + PostgreSQL |
| Stack front | React Vite + TypeScript + Tailwind |
| IA par défaut | Ollama local (Llama 3.1 8B ou Phi-3-mini) |
| Déploiement | Docker Compose |
| Données | Aucune sortie hors UE |
| Tout changement LLM | ADR obligatoire (cf. J2) |

---

## 📋 Récapitulatif visuel (une page)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PRODUCT VISION BOARD — EduTutor IA                   │
│                           29 juin 2026                                  │
├──────────────────────────────┬──────────────────────────────────────────┤
│  🌟 VISION STATEMENT         │  👥 TARGET GROUPS                        │
│                              │                                          │
│  Pour les étudiant·e·s du   │  1. Étudiant·e supérieur (primaire)      │
│  supérieur qui peinent à     │     18-28 ans, révision examens          │
│  réviser, EduTutor IA est    │                                          │
│  une app web qui génère des  │  2. Mme Lefèvre (primaire — J1)          │
│  quiz depuis leurs propres   │     42 ans, suivi 28 étudiants           │
│  cours via IA locale RGPD.   │                                          │
│  Contrairement aux MOOC IA,  │  3. Administrateur (interne)             │
│  chaque question est ancrée  │     Config LLM, gestion users            │
│  dans le document source.    │                                          │
├──────────────────────────────┼──────────────────────────────────────────┤
│  💡 NEEDS (Besoins)          │  📦 PRODUCT (Fonctionnalités clés)       │
│                              │                                          │
│  Étudiant :                  │  F1 : Auth email complète                │
│  • Générer quiz depuis PDF   │  F2 : Upload PDF/texte                   │
│  • Voir ses erreurs          │  F3 : Génération 10 QCM via Ollama       │
│  • Suivre sa progression     │  F4 : Correction automatique             │
│                              │  F5 : Score /10 + détail réponses        │
│  Enseignant :                │  F6 : Historique quiz                    │
│  • Dashboard élèves          │                                          │
│  • Repérer décrocheurs       │                                          │
│                              │                                          │
│  Admin :                     │                                          │
│  • Config LLM souverain      │                                          │
│  • Gestion utilisateurs      │                                          │
├──────────────────────────────┴──────────────────────────────────────────┤
│  📊 BUSINESS GOALS                                                      │
│                                                                         │
│  • 500 inscrits à 6 mois   • Rétention ≥ 60 % à 3 mois                │
│  • Satisfaction ≥ 4/5      • 0 donnée hors UE (RGPD)   • NPS ≥ 40     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Commentaire / preuve |
|---|:---:|---|
| La Vision tient en 1 phrase mémorable et survit aux releases | ☑ Oui | Vision Statement Geoffrey Moore en §🌟 : « générer des quiz ancrés dans le cours, IA locale souveraine ». |
| Les 3 niveaux de cibles (primaire / secondaire / tertiaire) sont décrits avec profil + volume + pain point | ☑ Oui | §👥 : étudiant (~2,7 M), enseignant (~770 k), établissement B2B (~7 500 lycées) + critère de décision. |
| Au moins 3 besoins par cible formulés en verbes d'action | ☑ Oui | §💡 : 3 besoins étudiant, 3 besoins enseignant, 2 besoins admin (format user story). |
| Le produit est décrit en 3-5 caractéristiques signature (pas une liste technique) | ☑ Oui | §📦 : F1–F6 orientées valeur + différenciateurs IA locale / RAG. |
| Les 6 features F1-F6 du MVP sont rappelées et des pistes Release 2 identifiées | ☑ Oui | §📦 (F1–F6) + Product Backlog §5 (catalogue R2). |
| Les Business Goals comportent au moins 3 KPI chiffrés et datés | ☑ Oui | §📊 : 500 inscrits/6 mois, rétention ≥ 60 %/3 mois, NPS ≥ 40/6 mois, 10 établissements/12 mois. |
| Les 4 concurrents sont cartographiés avec positionnement + limite | ☑ Oui | §🆚 : Wilgo, Quizlet AI, Khanmigo, Leo. |
| Les 3 différenciateurs sont argumentés au-delà du slogan | ☑ Oui | §🆚 : enseignant-first, ancrage RAG traçable, Ollama local RGPD. |
| Le document a été relu et validé par l'équipe | ☑ Oui | Revue d'équipe avant remise · validation PO en attente. |

---

## 📚 Références

**Incontournables**
- Cours Agile/Scrum (Mohamed EL AFRIT) — mohamedelafrit.com/teaching/Master_Classe_Agile/cours.html
- Scrum Guide officiel FR — scrumguides.org
- Site APOCAL'IPSSI — mohamedelafrit.com/teaching/APOCALIPSSI

**Spécifiques à ce document**
- Roman Pichler — Product Vision Board : https://www.romanpichler.com/tools/product-vision-board/
- Geoffrey Moore — *Crossing the Chasm* (formule de vision)
- Concurrents : Wilgo (wilgo.ai), Leo (iamleo.ai), Quizlet AI (quizlet.com), Khanmigo (khanmigo.ai)
- Volumes marché : MESR 2024 (étudiants), Éducation nationale 2024 (enseignants)

---

## 🔄 Convention de versionnement

- **v1.0** — version initiale produite lors du cadrage matinal (29/06/2026)
- **v1.x** — révisions mineures (typo, ajout d'item) après revue PO
- **v2.0** — révision majeure suite à une perturbation (changement de scope)
- Chaque version est commitée séparément avec un message Git explicite ; le statut « Validé PO » nécessite une trace écrite.

---

*Product Vision Board rédigé selon la méthode Roman Pichler — Vision Statement selon Geoffrey Moore (Crossing the Chasm)*  
*Dépôt : `/docs/cadrage/product-vision-board.md` — v1.0 — 29/06/2026*
