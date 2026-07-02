# Réponse à la demande d'accès RGPD — Hugo Petit (Art. 15)

> **Document** : Perturbation J3-bis — Réponse SAR (Subject Access Request)  
> **Rédigé par** : Dina CHAOUKI · Équipe n°6  
> **Date** : 02/07/2026  
> **Dépôt** : `docs/perturbations/j3bis-reponse-hugo-petit.md`

---

## Email de réponse

**De** : equipe6-dpo@edututoria.fr  
**À** : hugo.petit@test.local  
**Objet** : Réponse à votre demande d'accès à vos données personnelles (RGPD Art. 15) — Réf. SAR-2026-001  
**Date** : 02/07/2026

---

Monsieur Hugo Petit,

Nous accusons réception de votre demande d'accès à vos données personnelles du **30 juin 2026**, formulée conformément à l'article 15 du Règlement Général sur la Protection des Données (RGPD).

Après vérification de votre identité via l'adresse `hugo.petit@test.local`, nous vous communiquons ci-dessous l'intégralité des données personnelles que nous détenons à votre sujet.

---

### 1. Données transmises

Conformément à l'Art. 15 RGPD et à l'Art. 20 (droit à la portabilité), l'export complet de vos données est disponible au format **JSON** via le lien de téléchargement sécurisé ci-dessous, accessible avec vos identifiants :

> **Endpoint** : `GET https://edututoria.fr/api/accounts/me/export/`  
> **Formats disponibles** : JSON · CSV  
> **Valide** : 7 jours à compter de la date de cet email

Les données exportées incluent exhaustivement :

| Catégorie | Contenu |
|---|---|
| **Données de compte** | Email, date d'inscription, date de dernière connexion, statut de validation |
| **Cours uploadés** | Titres et métadonnées des documents soumis (les fichiers bruts sont supprimés après 90 jours) |
| **Quiz générés** | Liste des quiz, date de génération, titre du cours source |
| **Réponses et scores** | Vos réponses question par question, score /10, date de soumission |
| **Historique de progression** | Statistiques agrégées (score moyen, nombre de quiz, meilleur score) |
| **Signalements émis** | Néant — aucun signalement enregistré à votre nom |
| **Logs d'audit** | Dates de connexion (pseudonymisées après 12 mois) |

---

### 2. Informations sur le traitement de vos données

**Responsable du traitement** : EduTutor IA — equipe6@edututoria.fr *(entité fictive — contexte pédagogique POC)*

**Finalités** : fourniture du service de génération de quiz pédagogiques, suivi de progression, sécurité du compte.

**Base légale** : Art. 6(1)(b) RGPD — exécution du contrat de service.

**Durées de conservation** : détaillées dans notre [politique de rétention](../legal/retention.md) — compte actif conservé le temps de votre utilisation + 30 jours ; quiz et scores 24 mois ; logs techniques 12 mois.

**Transferts hors UE** : **aucun**. Le traitement IA est réalisé exclusivement en local (Ollama — serveur situé en France). Aucune donnée ne quitte l'Union Européenne.

---

### 3. Vos droits

Conformément au RGPD, vous disposez des droits suivants, que vous pouvez exercer à tout moment :

| Droit | Article RGPD | Comment l'exercer |
|---|---|---|
| **Rectification** | Art. 16 | Page Profil → Modifier mes informations |
| **Effacement** ("droit à l'oubli") | Art. 17 | Page Profil → Supprimer mon compte |
| **Limitation du traitement** | Art. 18 | Demande écrite au DPO |
| **Portabilité** | Art. 20 | Page Profil → Exporter mes données (JSON/CSV) |
| **Opposition** | Art. 21 | Demande écrite au DPO |
| **Réclamation CNIL** | — | [https://www.cnil.fr/fr/plaintes](https://www.cnil.fr/fr/plaintes) |

---

### 4. Contact DPO

Pour toute question complémentaire relative à vos données personnelles :

**Délégué à la Protection des Données (DPO)**  
EduTutor IA  
Email : `dpo@edututoria.fr` *(fictif — contexte POC)*  
Délai de réponse : 30 jours maximum (Art. 12 RGPD)

---

Nous restons à votre disposition pour toute question.

Cordialement,

**L'équipe EduTutor IA**  
equipe6-dpo@edututoria.fr

---

## Audit trail SAR — Réf. SAR-2026-001

| Champ | Valeur |
|---|---|
| **Identifiant demande** | SAR-2026-001 |
| **Demandeur** | hugo.petit@test.local |
| **Date de réception** | 30/06/2026 10h30 |
| **Statut** | ✅ Répondue |
| **Date de réponse** | 02/07/2026 |
| **Délai de traitement** | 2 jours (SLA 48h respecté) |
| **Données transmises** | Export JSON complet — 7 catégories |
| **Hash fichier export** | `sha256:à_calculer_à_la_génération` |

*Ce log doit être persisté en base via le modèle `DataRequest` (CA-J3B-6).*
