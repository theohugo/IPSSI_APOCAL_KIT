"""Tests minimaux pour l'app llm — K1.

Le ping est testé avec backend=mock pour éviter de dépendre d'Ollama.
"""
import pytest
from django.test import override_settings
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


@override_settings(LLM_BACKEND="mock")
def test_ping_in_mock_mode():
    response = APIClient().get("/api/llm/ping/")
    assert response.status_code == 200
    assert response.data["backend"] == "mock"
    assert response.data["ollama_alive"] is False
