"""
Modèles de l'app accounts.

[Note pédagogique] On garde le modèle User standard de Django (simple et
robuste), et on lui ajoute un Profil 1-pour-1 pour les infos métier qui ne sont
pas dans User — ici `email_verified` (l'utilisateur a-t-il cliqué le lien de
confirmation envoyé par email ?).

Choix d'architecture « email = identifiant » : à l'inscription, on met
username = email (voir SignupSerializer). Le login se fait donc par email, sans
backend d'authentification custom. C'est le compromis le plus simple pour un
kit pédagogique (un vrai produit utiliserait souvent un User personnalisé avec
USERNAME_FIELD = 'email').
"""

from django.conf import settings
from django.db import models


class Profile(models.Model):
    """Informations complémentaires attachées à un utilisateur."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    # Validation "soft" : le compte fonctionne même si l'email n'est pas vérifié,
    # mais un bandeau invite l'utilisateur à cliquer le lien de confirmation.
    email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Profile<{self.user.email or self.user.username}>"


def get_or_create_profile(user) -> Profile:
    """Récupère (ou crée) le profil d'un utilisateur.

    Pratique pour les comptes créés AVANT l'ajout du modèle Profile (ils n'ont
    pas encore de profil) : on le crée à la volée plutôt que de planter.
    """
    profile, _ = Profile.objects.get_or_create(user=user)
    return profile


# ---------------------------------------------------------------------------
# Perturbation J3-bis (SAR RGPD) — droit d'accès / portabilité
# ---------------------------------------------------------------------------


class DataRequest(models.Model):
    """Trace une demande d'accès aux données personnelles (SAR — RGPD art. 15/20).

    [Note pédagogique] Le RGPD impose de pouvoir répondre à une demande d'accès
    (« quelles données avez-vous sur moi ? ») et de portabilité (« rendez-les
    moi dans un format lisible par machine »). On garde une TRACE de chaque
    demande — sa date, son format, son issue — indépendamment du fichier exporté,
    pour prouver qu'on a bien traité la demande (obligation de « accountability »).
    """

    class Status(models.TextChoices):
        PROCESSING = "processing", "En cours"
        RESPONDED = "responded", "Répondue"
        FAILED = "failed", "Échec"

    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="data_requests",
        help_text="Utilisateur ayant demandé l'export de ses données.",
    )
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PROCESSING)
    requested_format = models.CharField(max_length=10, default="json")
    responded_at = models.DateTimeField(null=True, blank=True)
    # Empreinte SHA-256 du fichier exporté : preuve d'intégrité sans stocker les
    # données perso elles-mêmes (on n'archive PAS l'export côté serveur).
    export_sha256 = models.CharField(max_length=64, blank=True, default="")
    export_filename = models.CharField(max_length=255, blank=True, default="")
    response_size = models.PositiveIntegerField(null=True, blank=True)
    error_message = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-requested_at"]
        verbose_name = "Demande d'accès aux données (SAR)"
        verbose_name_plural = "Demandes d'accès aux données (SAR)"

    def __str__(self) -> str:
        return f"SAR<{self.requester.email or self.requester.username}>/{self.status}"


class AuditEvent(models.Model):
    """Journal minimal des événements RGPD sensibles liés à un utilisateur.

    [Note pédagogique] Pour l'« accountability » RGPD, on trace les actions
    sensibles (export de données, suppression de compte). C'est volontairement
    léger : un type d'événement, un message, un contexte JSON facultatif.
    """

    class Type(models.TextChoices):
        DATA_EXPORT = "data_export", "Export de données (SAR)"
        ACCOUNT_DELETED = "account_deleted", "Suppression de compte"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="audit_events",
        help_text="Utilisateur concerné par l'événement.",
    )
    event_type = models.CharField(max_length=40, choices=Type.choices)
    message = models.CharField(max_length=255, blank=True, default="")
    payload = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Événement d'audit"
        verbose_name_plural = "Événements d'audit"

    def __str__(self) -> str:
        return f"Audit<{self.user_id}:{self.event_type}>"
