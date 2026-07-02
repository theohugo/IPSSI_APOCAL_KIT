# Perturbation J3-bis — Réponse à la demande d'accès de M. Hugo Petit (RGPD Art. 15)

## 🗂️ Identification du document

| | |
|---|---|
| **Équipe** | n° 6 |
| **Membres** | Kahil MOKHTARI · Amine HADDANE · Souleymane FALL · Nikola MILOSAVLJEVIC · Dina CHAOUKI · Rayan ZEBAZE SAO · Hugo RAGUIN |
| **Artefact** | Perturbation J3-bis — Réponse écrite au demandeur (SAR) |
| **Version** | v1.0 |
| **Date** | 01/07/2026 |
| **Statut** | ✅ Réponse rédigée (dans le délai de 48 h) |
| **Rédacteur** | Souleymane FALL |

> Liens : [Export RGPD (SAR)](j3bis-rgpd.md) · [Politique de rétention](j3bis-politique-retention.md).

---

## Contexte

**M. Hugo Petit** (étudiant M2 Droit numérique) a soumis le **mercredi à 10h30** une **demande formelle d'accès** à ses données personnelles (RGPD **Article 15**), au format structuré, avec un **délai de réponse de 48 h**. Voici l'email de réponse professionnel envoyé en retour.

---

## ✉️ Email de réponse

> **De :** dpo@edututor-ia.fr
> **À :** hugo.petit@example.com
> **Objet :** Votre demande d'accès à vos données personnelles (RGPD Art. 15) — donnant suite
> **Date :** jeudi (dans les 48 h suivant votre demande)

Bonjour M. Petit,

Nous accusons **réception de votre demande d'accès** à vos données personnelles, formulée le mercredi à 10h30 au titre de l'**article 15 du RGPD**. Nous la traitons dans le **délai légal** (et sous 48 h comme vous l'avez demandé).

**Comment récupérer vos données**

Votre export complet est disponible **immédiatement et en autonomie**, depuis votre espace :

1. Connectez-vous à votre compte EduTutor IA ;
2. rendez-vous dans **Mon profil → Mes données** ;
3. cliquez sur **« Exporter mes données (JSON) »** (ou **ZIP**).

Techniquement, l'export est servi par l'endpoint authentifié `GET /api/accounts/me/export/` (formats `json` ou `zip`).

**Contenu de l'export** (format structuré, lisible par machine)

Le fichier contient l'intégralité des données que nous détenons sur vous, réparties en **6 catégories** :

1. **Compte** (identité, email, dates) ;
2. **Cours / quiz générés** (titres, textes sources) ;
3. **Réponses et scores** ;
4. **Signalements** (le cas échéant) ;
5. **Demandes d'accès** (historique de vos exports) ;
6. **Journal d'audit** (traçabilité de vos exports).

Un contrôle d'intégrité (empreinte **SHA-256**) est associé à chaque export. Nous **n'archivons pas** le fichier sur nos serveurs : il est généré à la demande.

**Vos autres droits**

Au-delà de l'accès (Art. 15), vous disposez également des droits de :

- **rectification** (Art. 16) — corriger une donnée inexacte, depuis *Mon profil* ;
- **effacement** (Art. 17) — supprimer votre compte et toutes vos données (*Zone de danger*) ;
- **limitation** du traitement (Art. 18) ;
- **portabilité** (Art. 20) — le format d'export ci-dessus y répond directement.

**Conservation**

Les durées de conservation par type de donnée sont détaillées dans notre [politique de rétention](j3bis-politique-retention.md).

Pour toute question, vous pouvez répondre à cet email (notre délégué à la protection des données, **dpo@edututor-ia.fr**), ou saisir la CNIL.

Bien cordialement,
**L'équipe EduTutor IA — Protection des données**

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-éval | Preuve |
|---|:---:|---|
| Accusé de réception + délai respecté | ☑ Oui | en-tête + 1er paragraphe (48 h). |
| Lien / modalité de téléchargement | ☑ Oui | bouton profil + `GET /api/accounts/me/export/`. |
| Explication du contenu (6 catégories) | ☑ Oui | section « Contenu de l'export ». |
| Mention des droits Art. 16/17/18/20 | ☑ Oui | section « Vos autres droits ». |
| Ton professionnel | ☑ Oui | ensemble de l'email. |

---

*Perturbation J3-bis — réponse au demandeur (M. Hugo Petit). Complète l'[export RGPD](j3bis-rgpd.md) et la [politique de rétention](j3bis-politique-retention.md).*
