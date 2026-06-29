# Personas — EduTutor IA

> Artefact de cadrage Jour 1 — APOCAL'IPSSI 2026
> Produit : **EduTutor IA** — assistant IA de révision, *enseignant-first*, génération ancrée dans les cours (RAG) et 100 % local (Ollama, RGPD).
> Lien : voir aussi le [Product Backlog](product-backlog.md).

---

## 1. Objet du document

Ce document décrit les **utilisateurs cibles** d'EduTutor IA afin d'orienter les décisions produit et la priorisation du backlog. Le positionnement est *enseignant-first*, mais la **cible primaire d'usage** sont les **étudiants du supérieur** qui révisent à partir de leurs cours (PDF/texte). On distingue donc :

- **Personas primaires** — pilotent le MVP (F1–F6) : l'étudiant qui révise.
- **Persona secondaire** — porte la vision *teacher-first* et les pistes Release 2.
- **Anti-persona** — qui le produit **ne** vise **pas**, pour cadrer le périmètre.

Chaque persona indique les **user stories** qu'il justifie (traçabilité avec le backlog).

---

## 2. Persona primaire #1 — Léa, l'étudiante qui révise dans l'urgence

| | |
|---|---|
| **Âge / situation** | 20 ans, étudiante en L2 Droit |
| **Aisance numérique** | Élevée (mobile-first), peu patiente face aux outils complexes |
| **Contexte** | Révise surtout le soir et la veille des partiels, à partir de PDF de cours |
| **Citation** | « J'ai 60 pages à réviser ce soir, je veux juste savoir si j'ai compris. » |

**Objectifs**
- Transformer rapidement un cours (PDF/texte) en quiz pour s'auto-évaluer.
- Identifier ses points faibles **avant** l'examen.
- Suivre sa progression d'une session à l'autre.

**Frustrations**
- Relire passivement sans savoir ce qui est acquis.
- Outils de révision génériques, déconnectés de **ses** cours.
- Saisir manuellement des fiches/QCM : trop long.

**Besoins → User stories**
- Upload PDF / coller du texte → **US-F2.1, US-F2.2**
- Générer 10 QCM ancrés dans le cours → **US-F3.1**
- Voir un score /10 + le détail des erreurs → **US-F5.1, US-F5.2**
- Retrouver l'historique de ses quiz → **US-F6.1**

**Scénario type** : Léa téléverse le PDF du chapitre, lance la génération, répond aux 10 QCM dans le métro, obtient 6/10 et voit les 4 questions ratées → elle sait quoi revoir.

---

## 3. Persona primaire #2 — Karim, l'étudiant méthodique en reconversion

| | |
|---|---|
| **Âge / situation** | 29 ans, étudiant en BTS SIO (reconversion pro) |
| **Aisance numérique** | Bonne, mais soucieux de la **confidentialité** de ses données |
| **Contexte** | Révise régulièrement, sur ordinateur, par sessions planifiées |
| **Citation** | « Je veux progresser dans la durée, pas bachoter — et savoir où vont mes données. » |

**Objectifs**
- Réviser de façon régulière et mesurer sa progression sur plusieurs semaines.
- Cibler ses révisions sur ses erreurs passées.
- S'assurer que ses documents restent **privés**.

**Frustrations**
- Outils qui envoient les contenus à des services cloud externes.
- Pas de suivi de l'évolution des scores dans le temps.
- Devoir recréer un compte / perdre son historique.

**Besoins → User stories**
- Compte fiable, email vérifié, mot de passe récupérable → **US-F1.1 à US-F1.5**
- Historique persistant (date, cours, score) → **US-F6.1, US-F6.2**
- Rejouer un quiz ciblé sur ses erreurs → **US-Q.1** (should)
- Garantie RGPD : LLM **local** (Ollama), aucune donnée envoyée au cloud → contrainte transverse (E7)

**Scénario type** : Karim se connecte chaque dimanche, consulte ses scores des 3 dernières semaines, relance un quiz sur le chapitre où il plafonne à 5/10.

---

## 4. Persona secondaire — Mme Nadia, l'enseignante (vision *teacher-first*)

| | |
|---|---|
| **Âge / situation** | 41 ans, enseignante en IUT |
| **Aisance numérique** | Moyenne, peu de temps à consacrer à de nouveaux outils |
| **Contexte** | Veut proposer de l'auto-évaluation à ses étudiants à partir de **ses** supports |
| **Citation** | « Je veux des quiz fidèles à mon cours, sans y passer mes soirées. » |

**Objectifs**
- Générer des QCM alignés sur ses propres supports de cours.
- Offrir un outil d'entraînement à ses étudiants.
- (R2) Suivre la progression d'une classe.

**Frustrations**
- Créer des QCM manuellement est chronophage.
- Outils pensés pour l'étudiant, jamais pour le pédagogue.
- Crainte sur la conformité RGPD des données des étudiants.

**Besoins → User stories**
- Génération ancrée dans les supports (RAG) → **US-F3.1**, renforcé en **US-R2.1**
- Tableau de bord enseignant / suivi de classe → **US-R2.2** (Release 2)
- Niveaux de difficulté des QCM → **US-R2.3** (Release 2)

**Note de cadrage** : ce persona porte la **différenciation produit** (*enseignant-first*) mais ses besoins relèvent majoritairement de la **Release 2**. Il oriente la vision, pas le MVP de la semaine.

---

## 5. Anti-persona — Thomas, le candidat à un concours généraliste

| | |
|---|---|
| **Profil** | Cherche une banque de QCM **toute prête**, sans fournir de cours |
| **Attente** | Du contenu générique de culture générale, du classement entre candidats, du gamification poussé |

**Pourquoi hors cible** : EduTutor IA génère des quiz **à partir des documents de l'utilisateur** (ancrage RAG), pas une base de questions universelle. Le produit ne vise ni la compétition entre utilisateurs, ni le contenu générique → cf. **US-W.1/W.2** (Won't have). Cadrer cet anti-persona évite de dériver vers un « Quizlet généraliste ».

---

## 6. Synthèse priorisation

| Persona | Type | Pilote | Stories clés |
|---------|------|--------|--------------|
| **Léa** | Primaire | MVP F2/F3/F5/F6 | US-F2.x, US-F3.1, US-F5.x, US-F6.1 |
| **Karim** | Primaire | MVP F1/F6 + RGPD | US-F1.x, US-F6.x, US-Q.1 |
| **Nadia** | Secondaire | Vision R2 | US-F3.1, US-R2.1/2.2/2.3 |
| **Thomas** | Anti-persona | Hors périmètre | US-W.x |

**À retenir pour le Product Owner** : le **Sprint 1 sert d'abord Léa et Karim** (les deux étudiants). Les besoins de Nadia nourrissent le Release Planning R2 mais ne doivent pas entrer dans le périmètre must-have de la semaine.

---

*Document vivant — à affiner après les premiers retours utilisateurs. Source de vérité du périmètre : GitHub Issues & Project du dépôt.*
