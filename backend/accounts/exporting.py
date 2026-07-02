"""Construction des exports RGPD (JSON / ZIP) pour un utilisateur.

[Note pédagogique] Le droit à la portabilité (RGPD art. 20) impose de rendre à
l'utilisateur SES données dans un format « structuré, couramment utilisé et
lisible par machine ». On rassemble donc ici, en un seul endroit, tout ce que
le produit stocke sur une personne : son compte, son profil, ses quiz, ses
questions et ses réponses. On n'expose JAMAIS de données d'un autre utilisateur.
"""

from __future__ import annotations

import io
import json
import zipfile
from dataclasses import dataclass
from hashlib import sha256

from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.utils import timezone

from quizzes.models import Quiz

from .models import AuditEvent, DataRequest, get_or_create_profile

# Formats d'export supportés (droit à la portabilité).
SUPPORTED_FORMATS = ("json", "zip")


@dataclass(slots=True)
class ExportArtifact:
    """Fichier d'export prêt à être renvoyé au client."""

    content: bytes
    content_type: str
    filename: str
    sha256_hex: str


def _account_payload(user: User) -> dict:
    profile = get_or_create_profile(user)
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "date_joined": user.date_joined,
        "is_active": user.is_active,
        "is_staff": user.is_staff,
        "profile": {
            "email_verified": profile.email_verified,
            "created_at": profile.created_at,
        },
    }


def _quizzes_payload(user: User) -> list[dict]:
    quizzes = (
        Quiz.objects.filter(user=user)
        .annotate(question_count=Count("questions"))
        .prefetch_related("questions")
        .order_by("-created_at")
    )
    return [
        {
            "id": quiz.id,
            "title": quiz.title,
            "source_text": quiz.source_text,
            "score": quiz.score,
            "created_at": quiz.created_at,
            "updated_at": quiz.updated_at,
            "question_count": quiz.question_count,
            "questions": [
                {
                    "index": q.index,
                    "prompt": q.prompt,
                    "options": q.options,
                    "correct_index": q.correct_index,
                    "selected_index": q.selected_index,
                }
                for q in quiz.questions.all()
            ],
        }
        for quiz in quizzes
    ]


def _answers_payload(user: User) -> list[dict]:
    """Réponses données par l'utilisateur (questions auxquelles il a répondu)."""
    answered = Quiz.objects.filter(user=user).prefetch_related("questions").order_by("-created_at")
    rows: list[dict] = []
    for quiz in answered:
        for q in quiz.questions.all():
            if q.selected_index is not None:
                rows.append(
                    {
                        "quiz_id": quiz.id,
                        "quiz_title": quiz.title,
                        "index": q.index,
                        "selected_index": q.selected_index,
                        "correct_index": q.correct_index,
                        "correct": q.selected_index == q.correct_index,
                    }
                )
    return rows


def _data_requests_payload(user: User) -> list[dict]:
    return [
        {
            "requested_at": dr.requested_at,
            "status": dr.status,
            "requested_format": dr.requested_format,
            "responded_at": dr.responded_at,
            "export_sha256": dr.export_sha256,
            "export_filename": dr.export_filename,
            "response_size": dr.response_size,
        }
        for dr in DataRequest.objects.filter(requester=user).order_by("-requested_at")
    ]


def _audit_events_payload(user: User) -> list[dict]:
    return [
        {
            "event_type": ev.event_type,
            "message": ev.message,
            "payload": ev.payload,
            "created_at": ev.created_at,
        }
        for ev in AuditEvent.objects.filter(user=user).order_by("-created_at")
    ]


def _reports_payload(user: User) -> list[dict]:
    """Signalements émis par l'utilisateur.

    Aucun modèle de signalement n'existe encore dans le produit (fonctionnalité
    prévue). On expose donc une liste vide plutôt qu'une donnée factice : la
    catégorie « signalements » demandée par l'énoncé J3-bis est bien présente.
    """
    return []


def build_export_payload(user: User) -> dict:
    """Construit l'objet complet exportable pour le compte donné.

    Couvre les 6 catégories demandées (SAR J3-bis) : compte, quiz (cours +
    questions), réponses, signalements, demandes d'accès et journal d'audit.
    """
    return {
        "exported_at": timezone.now(),
        "notice": (
            "Export RGPD (droit d'accès et à la portabilité) généré par EduTutor IA. "
            "Ce fichier contient toutes les données personnelles associées à votre compte."
        ),
        "account": _account_payload(user),
        "quizzes": _quizzes_payload(user),
        "answers": _answers_payload(user),
        "reports": _reports_payload(user),
        "data_requests": _data_requests_payload(user),
        "audit_logs": _audit_events_payload(user),
    }


def build_export_artifact(user: User, output_format: str = "json") -> ExportArtifact:
    """Sérialise l'export dans le format demandé (`json` ou `zip`)."""
    if output_format not in SUPPORTED_FORMATS:
        raise ValueError(f"Format d'export non supporté : {output_format!r}")

    payload = build_export_payload(user)
    stamp = timezone.now().strftime("%Y%m%d")
    base = f"edututor-export-{user.username}-{stamp}"

    if output_format == "zip":
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, content in payload.items():
                archive.writestr(
                    f"{name}.json",
                    json.dumps(content, ensure_ascii=False, indent=2, cls=DjangoJSONEncoder),
                )
        content = buffer.getvalue()
        content_type = "application/zip"
        filename = f"{base}.zip"
    else:
        content = json.dumps(payload, ensure_ascii=False, indent=2, cls=DjangoJSONEncoder).encode(
            "utf-8"
        )
        content_type = "application/json"
        filename = f"{base}.json"

    return ExportArtifact(
        content=content,
        content_type=content_type,
        filename=filename,
        sha256_hex=sha256(content).hexdigest(),
    )
