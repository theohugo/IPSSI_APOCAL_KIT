"""Journalisation des événements RGPD sensibles (perturbation J3-bis).

[Note pédagogique] On centralise ici l'écriture d'un `AuditEvent` pour ne pas
disperser la logique dans les vues. « Accountability » RGPD : garder une trace
des accès/exports/suppressions de données personnelles.
"""

from __future__ import annotations

import logging

from django.contrib.auth.models import User

from .models import AuditEvent

logger = logging.getLogger(__name__)


def record_event(user: User, event_type: str, message: str = "", **payload) -> AuditEvent:
    """Enregistre un événement d'audit pour `user`.

    Best-effort : une erreur d'écriture d'audit ne doit jamais casser l'action
    métier (l'export ou la suppression reste prioritaire). On log alors l'échec.
    """
    try:
        return AuditEvent.objects.create(
            user=user,
            event_type=event_type,
            message=message,
            payload=payload or {},
        )
    except Exception:  # pragma: no cover - garde-fou défensif
        logger.exception("Échec d'écriture d'un AuditEvent (%s) pour user %s", event_type, user.pk)
        raise
