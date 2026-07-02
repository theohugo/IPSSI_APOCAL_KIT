"""Tests pédagogiques pour l'app accounts.

Ces tests servent d'exemples : signup, login, logout, accès protégé.
Lancez : pytest accounts/
"""

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(
        username="alice", email="alice@test.com", password="motdepasse123"
    )


def test_signup_creates_user(client):
    # Lot 3 : inscription par EMAIL (username = email en interne).
    response = client.post(
        "/api/accounts/signup/",
        {
            "email": "bob@test.com",
            "password": "motdepasse123",
        },
        format="json",
    )
    assert response.status_code == 201, response.data
    assert User.objects.filter(email="bob@test.com").exists()


def test_signup_requires_email(client):
    response = client.post(
        "/api/accounts/signup/",
        {"password": "motdepasse123"},
        format="json",
    )
    assert response.status_code == 400


def test_login_returns_token(client, user):
    response = client.post(
        "/api/accounts/login/",
        {"email": "alice@test.com", "password": "motdepasse123"},
        format="json",
    )
    assert response.status_code == 200, response.data
    assert "token" in response.data
    assert response.data["user"]["email"] == "alice@test.com"


def test_login_with_wrong_password(client, user):
    response = client.post(
        "/api/accounts/login/",
        {"email": "alice@test.com", "password": "wrong"},
        format="json",
    )
    assert response.status_code == 400


def test_me_requires_auth(client):
    response = client.get("/api/accounts/me/")
    assert response.status_code in (401, 403)


def test_me_with_token(client, user):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.get("/api/accounts/me/")
    assert response.status_code == 200
    assert response.data["username"] == "alice"


def test_logout_invalidates_token(client, user):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.post("/api/accounts/logout/")
    assert response.status_code == 204
    # Le token n'existe plus
    assert not Token.objects.filter(key=token.key).exists()


# ---------------------------------------------------------------------------
# Perturbation J3-bis (SAR RGPD) — export des données personnelles
# ---------------------------------------------------------------------------


def _quiz_for(user, title="Cours de biologie"):
    """Crée un quiz + une question répondue pour l'utilisateur (données à exporter)."""
    from quizzes.models import Question, Quiz

    quiz = Quiz.objects.create(user=user, title=title, source_text="La photosynthèse…", score=8)
    Question.objects.create(
        quiz=quiz,
        index=1,
        prompt="Que produit la photosynthèse ?",
        options=["O2", "N2", "CO2", "He"],
        correct_index=0,
        selected_index=0,
    )
    return quiz


def test_data_export_requires_auth(client):
    response = client.post("/api/accounts/data-export/", {}, format="json")
    assert response.status_code in (401, 403)


def test_data_export_returns_user_data(client, user):
    import json

    from accounts.models import AuditEvent, DataRequest

    _quiz_for(user)
    client.force_authenticate(user=user)

    response = client.post("/api/accounts/data-export/", {"format": "json"}, format="json")
    assert response.status_code == 200, response.content
    assert response["Content-Type"] == "application/json"
    assert "attachment;" in response["Content-Disposition"]

    payload = json.loads(
        b"".join(response.streaming_content) if response.streaming else response.content
    )
    assert payload["account"]["email"] == "alice@test.com"
    assert len(payload["quizzes"]) == 1
    assert payload["quizzes"][0]["title"] == "Cours de biologie"
    assert payload["answers"][0]["correct"] is True

    # La demande est tracée (DataRequest « responded ») + un AuditEvent d'export.
    dr = DataRequest.objects.get(requester=user)
    assert dr.status == DataRequest.Status.RESPONDED
    assert dr.export_sha256 and dr.export_sha256 == response["X-Export-SHA256"]
    assert AuditEvent.objects.filter(user=user, event_type="data_export").exists()


def test_data_export_zip_format(client, user):
    _quiz_for(user)
    client.force_authenticate(user=user)
    response = client.post("/api/accounts/data-export/", {"format": "zip"}, format="json")
    assert response.status_code == 200
    assert response["Content-Type"] == "application/zip"


def test_data_export_rejects_unknown_format(client, user):
    client.force_authenticate(user=user)
    response = client.post("/api/accounts/data-export/", {"format": "pdf"}, format="json")
    assert response.status_code == 400


def test_data_export_isolates_other_users(client, user):
    """Un export ne doit JAMAIS contenir les données d'un autre utilisateur."""
    import json

    other = User.objects.create_user(username="bob", email="bob@test.com", password="motdepasse123")
    _quiz_for(other, title="Cours secret de Bob")
    _quiz_for(user, title="Cours d'Alice")

    client.force_authenticate(user=user)
    response = client.post("/api/accounts/data-export/", {"format": "json"}, format="json")
    body = (
        b"".join(response.streaming_content) if response.streaming else response.content
    ).decode()
    assert "Cours d'Alice" in body
    assert "Cours secret de Bob" not in body
    payload = json.loads(body)
    assert all(q["title"] != "Cours secret de Bob" for q in payload["quizzes"])


def test_data_export_history(client, user):
    client.force_authenticate(user=user)
    client.post("/api/accounts/data-export/", {"format": "json"}, format="json")
    response = client.get("/api/accounts/data-export/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["status"] == "responded"


# --- Endpoint canonique de l'énoncé : GET /api/accounts/me/export/ ---


def test_me_export_requires_auth(client):
    response = client.get("/api/accounts/me/export/")
    assert response.status_code in (401, 403)


def test_me_export_get_returns_6_categories(client, user):
    import json

    from accounts.models import AuditEvent, DataRequest

    _quiz_for(user)
    client.force_authenticate(user=user)

    response = client.get("/api/accounts/me/export/")
    assert response.status_code == 200, response.content
    assert response["Content-Type"] == "application/json"
    assert "attachment;" in response["Content-Disposition"]

    payload = json.loads(response.content)
    # Les 6 catégories demandées par l'énoncé J3-bis doivent être présentes.
    for key in ("account", "quizzes", "answers", "reports", "data_requests", "audit_logs"):
        assert key in payload, f"catégorie manquante : {key}"
    assert payload["account"]["email"] == "alice@test.com"
    assert payload["quizzes"][0]["title"] == "Cours de biologie"

    # GET produit bien la trace (DataRequest responded + AuditEvent).
    dr = DataRequest.objects.get(requester=user)
    assert dr.status == DataRequest.Status.RESPONDED
    assert dr.export_sha256 == response["X-Export-SHA256"]
    assert AuditEvent.objects.filter(user=user, event_type="data_export").exists()


def test_me_export_zip_format(client, user):
    client.force_authenticate(user=user)
    response = client.get("/api/accounts/me/export/?fmt=zip")
    assert response.status_code == 200
    assert response["Content-Type"] == "application/zip"


def test_me_export_rejects_unknown_format(client, user):
    client.force_authenticate(user=user)
    response = client.get("/api/accounts/me/export/?fmt=pdf")
    assert response.status_code == 400
