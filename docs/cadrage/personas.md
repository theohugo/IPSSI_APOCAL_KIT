# Personas — EduTutor IA

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Sprint concerné** | Cadrage |
| **Artefact** | 2 sur 7 — Personas |
| **Version** | v1.1 (mise à jour perturbation J1) |
| **Date de remise** | 29/06/2026 |
| **Statut** | Draft (à valider PO) |
| **Rédacteur** | Hugo RAGUIN |
| **Fichier** | `equipe-6-personas-v1.1` |

> Produit : **EduTutor IA** — assistant IA de révision, *enseignant-first*, génération ancrée dans les cours (RAG) et 100 % local (Ollama, RGPD).
> Liens : [Product Vision Board](product-vision-board.md) · [Product Backlog](product-backlog.md) · [Perturbation J1 — Produit](perturbations/j1-produit.md).

---

## 1. Objet du document

Ce document décrit les **utilisateurs cibles** d'EduTutor IA afin d'orienter les décisions produit et la priorisation du backlog.

> **Mise à jour suite à la perturbation J1 (Produit).** Le Product Owner a introduit la persona enseignante **Mme Sophie Lefèvre** et l'a positionnée comme **cible principale, au même niveau que l'étudiant**. EduTutor IA sert désormais **deux familles de personas primaires** :
>
> - les **étudiants** qui révisent à partir de leurs cours (usage quotidien) ;
> - l'**enseignante** qui pilote la révision de sa classe (suivi, repérage, conseils).
>
> Détail et décision : voir [Perturbation J1 — Produit](perturbations/j1-produit.md).

On distingue donc :

- **Personas primaires** — pilotent le MVP. Deux usages : l'étudiant qui révise (F1–F6) **et** l'enseignante qui suit sa classe (Espace enseignant).
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

## 4. Persona primaire #3 — Mme Sophie Lefèvre, l'enseignante qui pilote sa classe

> **Persona issue de la perturbation J1 (Produit).** Initialement présentée par le PO comme cible secondaire, elle est désormais **cible principale, au même niveau que l'étudiant**. Ses besoins remontent en conséquence dans le périmètre **must-have / Release 1** (voir [Perturbation J1](perturbations/j1-produit.md)).

| | |
|---|---|
| **Âge / situation** | 42 ans, enseignante en BTS Communication à Lyon |
| **Aisance numérique** | Moyenne, peu de temps à consacrer à de nouveaux outils |
| **Contexte** | Encadre **28 étudiants** en révision d'examens ; veut un outil de suivi à partir de **ses** supports |
| **Citation** | « C'est exactement l'outil qu'il me faut pour suivre la progression de mes 28 étudiants en révision d'examens. Je veux pouvoir voir leurs scores, repérer ceux qui décrochent, et leur envoyer des conseils. » |

**Objectifs**
- Suivre la **progression** de ses 28 étudiants sur leurs révisions.
- **Repérer rapidement les décrocheurs** (objectif : en 3 clics).
- **Envoyer des conseils ciblés** aux étudiants en difficulté.
- Proposer des quiz **fidèles à ses propres supports de cours** (RAG).

**Frustrations**
- Aucune vue d'ensemble : impossible de savoir qui décroche sans interroger chaque étudiant.
- Créer des QCM manuellement est chronophage.
- Outils pensés uniquement pour l'étudiant, jamais pour le pédagogue.
- Crainte sur la conformité RGPD des données de ses étudiants.

**Besoins → User stories** *(nouvelles stories Espace enseignant, must-have suite à la perturbation J1)*
- Tableau de bord enseignant : scores et progression de la classe → **US-T.1**
- Repérage des décrocheurs en ≤ 3 clics (tri/alerte sur scores faibles) → **US-T.2**
- Envoi de conseils ciblés à un étudiant en difficulté → **US-T.3**
- Génération de QCM ancrée dans ses supports (RAG) → **US-F3.1** (mutualisé avec les étudiants)
- Garantie RGPD : LLM **local** (Ollama), données des étudiants non envoyées au cloud → contrainte transverse (E7)

**Scénario type** : Mme Lefèvre se connecte à l'espace enseignant, ouvre le tableau de bord de sa classe, repère en 3 clics les 4 étudiants sous la moyenne sur le dernier chapitre, et leur envoie un conseil de révision ciblé.

**Note de cadrage** : ce persona porte la **différenciation produit** (*enseignant-first*). Avec la perturbation J1, le tableau de bord de classe, le repérage des décrocheurs et l'envoi de conseils **entrent dans le périmètre prioritaire** (et ne sont plus repoussés en Release 2). Le backlog (GitHub Issues / Product Backlog) doit être actualisé en conséquence.

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
| **Léa** | Primaire (étudiant) | MVP F2/F3/F5/F6 | US-F2.x, US-F3.1, US-F5.x, US-F6.1 |
| **Karim** | Primaire (étudiant) | MVP F1/F6 + RGPD | US-F1.x, US-F6.x, US-Q.1 |
| **Sophie Lefèvre** | Primaire (enseignante, perturbation J1) | MVP Espace enseignant + F3 | US-T.1, US-T.2, US-T.3, US-F3.1 |
| **Thomas** | Anti-persona | Hors périmètre | US-W.x |

**À retenir pour le Product Owner** : depuis la perturbation J1, le **Sprint 1 sert deux cibles principales** — les étudiants (Léa, Karim) **et** l'enseignante (Mme Lefèvre). Les fonctionnalités de suivi de classe, autrefois en Release 2, font désormais partie du périmètre prioritaire.

---

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Commentaire / preuve |
|---|:---:|---|
| Chaque persona a un profil concret (âge, situation, aisance numérique, contexte) | ☑ Oui | Léa, Karim, Mme Lefèvre décrits en table profil + citation. |
| Les objectifs et frustrations sont explicites | ☑ Oui | Sections « Objectifs » et « Frustrations » pour chaque persona. |
| Chaque persona est tracé vers des user stories du backlog | ☑ Oui | « Besoins → User stories » (US-F1.x à US-T.3). |
| Un anti-persona cadre le hors-périmètre | ☑ Oui | §5 Thomas (candidat concours généraliste) → US-W.x. |
| La perturbation J1 est intégrée et tracée | ☑ Oui | Mme Sophie Lefèvre repositionnée primaire (§4) + lien perturbation J1. |
| Une synthèse de priorisation oriente le PO | ☑ Oui | §6 table de synthèse + note d'arbitrage PO. |
| Le document a été relu et validé par l'équipe | ☑ Oui | Revue d'équipe avant remise · validation PO en attente. |

---

## 📚 Références

- Cours Agile/Scrum (Mohamed EL AFRIT) — mohamedelafrit.com/teaching/APOCALIPSSI
- Alan Cooper — *The Inmates Are Running the Asylum* (méthode des personas)
- Roman Pichler — personas & target groups (romanpichler.com)
- Sources internes : [Product Vision Board](product-vision-board.md) · [Customer Journey Map](03_customer_journey_map.md) · [Perturbation J1](perturbations/j1-produit.md)

---

## 🔄 Convention de versionnement

- **v1.0** — version initiale (cadrage matinal, 29/06/2026)
- **v1.1** — intégration de la perturbation J1 : Mme Lefèvre repositionnée cible primaire
- **v2.0** — révision majeure suite à une prochaine perturbation (changement de scope)

---

*Document vivant — à affiner après les premiers retours utilisateurs. Source de vérité du périmètre : GitHub Issues & Project du dépôt.*
