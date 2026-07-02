# Politique de rétention des données personnelles — EduTutor IA

> **Document légal** · Perturbation J3-bis — RGPD Art. 5(1)(e) · Semaine APOCAL'IPSSI 2026  
> **Équipe** : n° 6  
> **Rédigé par** : Dina CHAOUKI  
> **Date** : 02/07/2026  
> **Version** : v1.0  
> **Références légales** : RGPD Art. 5, 6, 13, 17 · Recommandations CNIL 2024

---

## 1. Durées de conservation par type de donnée

| Type de donnée | Durée de conservation | Déclencheur de suppression |
|---|---|---|
| **Données de compte** (email, mot de passe haché, date d'inscription) | Durée de vie du compte actif + **30 jours** après suppression | Demande de suppression Art.17 ou inactivité 24 mois |
| **Documents uploadés** (PDF, textes de cours) | **90 jours** après génération du quiz associé | Suppression automatique par tâche planifiée (cron) |
| **Quiz générés** (questions, options, correct_index) | **24 mois** à compter de la date de génération | Suppression du compte ou demande Art.17 |
| **Réponses aux quiz et scores** | **24 mois** à compter de la date de soumission | Suppression du compte ou demande Art.17 |
| **Historique de progression** (statistiques, KPIs) | **24 mois** | Suppression du compte ou demande Art.17 |
| **Logs techniques** (connexions, erreurs, accès API) | **12 mois** (recommandation CNIL) | Rotation automatique par cron mensuel |
| **Logs d'audit SAR** (demandes d'accès, exports) | **36 mois** (prescription civile) | Suppression manuelle par DPO uniquement |
| **Emails de validation / reset** (tokens) | **24 heures** après émission ou utilisation | Expiration automatique en base |

> **Principe de minimisation (RGPD Art. 5(1)(c))** : EduTutor IA ne collecte que les données strictement nécessaires à la fourniture du service. Les documents uploadés ne sont jamais transmis à des services tiers — traitement exclusivement local (Ollama, RGPD conforme).

---

## 2. Motifs légaux de conservation (base juridique Art. 6 RGPD)

| Type de donnée | Base légale | Justification |
|---|---|---|
| **Données de compte** | Art. 6(1)(b) — **Exécution du contrat** | Nécessaire pour fournir le service (connexion, identification, accès aux quiz) |
| **Documents uploadés** | Art. 6(1)(b) — **Exécution du contrat** | Nécessaire pour générer le quiz demandé par l'utilisateur |
| **Quiz et réponses** | Art. 6(1)(b) — **Exécution du contrat** | Constitue le service rendu (résultat, correction, historique) |
| **Historique de progression** | Art. 6(1)(a) — **Consentement** | L'utilisateur choisit d'activer le suivi de progression (opt-in à l'inscription) |
| **Logs techniques** | Art. 6(1)(f) — **Intérêt légitime** | Sécurité du service, détection des abus, débogage (intérêt légitime documenté) |
| **Logs d'audit SAR** | Art. 6(1)(c) — **Obligation légale** | Preuve de conformité CNIL — obligation de traçabilité des demandes Art.15 |

> **Note** : EduTutor IA ne pratique **aucun profilage automatisé** au sens de l'Art. 22 RGPD. Les données ne sont pas vendues, louées ni cédées à des tiers.

---

## 3. Modalités de suppression (Art. 17 — Droit à l'effacement)

### 3.1 Suppression automatique (sans action utilisateur)

- **Documents uploadés** : suppression automatique 90 jours après la génération du quiz (cron quotidien).
- **Tokens d'email** : expiration automatique 24h après émission.
- **Logs techniques** : rotation mensuelle, conservation maximale 12 mois.

### 3.2 Suppression à la demande de l'utilisateur (Art. 17)

L'utilisateur peut supprimer son compte depuis la **page Profil** → "Supprimer mon compte". Cette action déclenche :

1. **Suppression immédiate** : données de compte, documents uploadés, quiz, réponses, scores, historique.
2. **Pseudonymisation** des logs techniques (remplacement de l'email par un hash irréversible) — conservation 12 mois pour obligations de sécurité.
3. **Conservation** des logs d'audit SAR pendant 36 mois (obligation légale Art. 6(1)(c)).
4. **Confirmation** par email à l'adresse enregistrée dans les 72 heures.

### 3.3 Demande d'accès / portabilité (Art. 15 / Art. 20)

L'utilisateur peut exporter l'intégralité de ses données via :
- **Frontend** : page Profil → "Exporter mes données" (téléchargement JSON/ZIP)
- **API** : `GET /api/accounts/me/export/?fmt=json|zip` (authentification requise)

Le fichier export inclut : données de compte, quiz générés, réponses, scores, historique, signalements.

### 3.4 Contact DPO

Pour toute demande relative à vos données personnelles :  
**DPO EduTutor IA** : `dpo@edututor-ia.fr` *(contact fictif — contexte pédagogique)*  
Délai de réponse : **30 jours** maximum (Art. 12 RGPD), **48h** pour les demandes SAR en phase POC.

---

*Politique de rétention v1.0 — EduTutor IA — 02/07/2026*  
*Dépôt : `docs/legal/retention.md`*
