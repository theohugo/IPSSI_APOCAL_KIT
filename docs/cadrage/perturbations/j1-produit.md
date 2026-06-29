# Perturbation J1 — Produit : Mme Sophie Lefèvre devient cible principale

> Journal de perturbation — APOCAL'IPSSI 2026
> Catégorie : **Produit** · Jour : **J1** · Décidé par : le **Product Owner** (animateur pédagogique)
> Liens : [Personas](../personas.md) · [Product Backlog](../product-backlog.md)
> Source : énoncé du cours — <https://mohamedelafrit.com/teaching/APOCALIPSSI/pages/perturbations/j1-produit.php>

---

## 1. Contexte

Au cours de la semaine APOCAL'IPSSI, le Product Owner injecte des **perturbations** simulant la vie réelle d'un produit (nouvelle contrainte, changement de cap, nouvelle partie prenante). La première, en J1, fait apparaître une **persona enseignante** jusque-là absente du cadrage initial centré sur l'étudiant.

## 2. L'annonce (énoncé du cours)

Le PO présente une nouvelle persona à intégrer : **Mme Sophie Lefèvre, 42 ans, enseignante en BTS Communication à Lyon**.

> « C'est exactement l'outil qu'il me faut pour suivre la progression de mes 28 étudiants en révision d'examens. Je veux pouvoir voir leurs scores, repérer ceux qui décrochent, et leur envoyer des conseils. »

Trois besoins explicites se dégagent :

1. **Suivre la progression** de ses 28 étudiants en révision d'examens.
2. **Repérer rapidement les décrocheurs** (objectif : en 3 clics).
3. **Envoyer des conseils ciblés** aux étudiants en difficulté.

## 3. Décision de l'équipe

Mme Lefèvre est **élevée au rang de persona principale, au même niveau que l'étudiant**. EduTutor IA cible désormais **deux familles de personas primaires** : les étudiants (usage de révision) et l'enseignante (pilotage de classe).

| Avant J1 | Après la perturbation J1 |
|---|---|
| Étudiant = unique cible principale | Étudiant **et** enseignante = cibles principales |
| Suivi de classe / dashboard envisagés en Release 2 | Suivi de classe **remonté en must-have / Release 1** |
| Persona enseignante absente du cadrage | Persona **Mme Sophie Lefèvre** documentée et priorisée |

> **Note** : l'énoncé écrit du cours qualifie initialement Mme Lefèvre de « cible secondaire ». La perturbation annoncée en séance l'a **promue cible principale, au même niveau que l'étudiant** — c'est cette consigne qui fait foi pour notre cadrage. L'écart est assumé et tracé ici.

## 4. Impacts

**Sur les personas** — Ajout de Mme Sophie Lefèvre comme **persona primaire #3** dans [personas.md](../personas.md) (section 4 et synthèse §6).

**Sur le périmètre / backlog** — Création d'un **Espace enseignant** et remontée des stories de suivi de classe en priorité :

| Story | Intitulé | Besoin couvert | Priorité (post-J1) |
|---|---|---|---|
| **US-T.1** | Tableau de bord enseignant : scores et progression de la classe | Suivre la progression | Must-have |
| **US-T.2** | Repérage des décrocheurs en ≤ 3 clics (tri / alerte sur scores faibles) | Repérer les décrocheurs | Must-have |
| **US-T.3** | Envoi de conseils ciblés à un étudiant en difficulté | Envoyer des conseils | Must-have |
| **US-F3.1** | Génération de QCM ancrée dans les supports (RAG) | Quiz fidèles au cours | Must-have (mutualisé étudiants) |

**Contrainte transverse** — Le suivi porte sur des **données d'étudiants** : la garantie RGPD (LLM **local** via Ollama, aucune donnée envoyée au cloud — E7) devient d'autant plus structurante.

## 5. MoSCoW (mise à jour)

- **Must** : US-T.1, US-T.2, US-T.3 (Espace enseignant), US-F3.1 (RAG).
- **Should** : niveaux de difficulté des QCM côté enseignant.
- **Could** : export des résultats de classe.
- **Won't (cette release)** : messagerie temps réel enseignant↔étudiant, classement inter-classes.

## 6. Traçabilité

- Personas : [personas.md §4](../personas.md) — Persona primaire #3.
- Backlog : stories **US-T.1 / US-T.2 / US-T.3** à créer/promouvoir dans GitHub Issues & Project.
- Source de vérité du périmètre : GitHub Issues & Project du dépôt.

---

*Document vivant — un fichier par perturbation dans ce dossier `perturbations/`.*
