"""
Tests de la boucle de retry Ollama (T-J2.6, perturbation J2).

Le correctif J2 rejoue jusqu'à MAX_RETRIES fois la génération quand le LLM
dévie du format « 10 QCM ». On vérifie ici les trois comportements clés sans
appeler un vrai Ollama (on monkeypatche `_call_ollama`) :

  1. succès au 1er coup                       → 1 appel, quiz renvoyé ;
  2. échecs transitoires puis succès          → on réessaie et on finit par réussir ;
  3. échecs jusqu'au bout                      → LLMError après MAX_RETRIES appels.
"""

import json

import pytest

from llm.services.base import LLMError
from llm.services.ollama_client import MAX_RETRIES, OllamaLLMClient


def _valid_raw() -> str:
    """Réponse LLM brute valide (10 QCM bien formés)."""
    return json.dumps(
        {
            "questions": [
                {
                    "prompt": f"Question {i} ?",
                    "options": ["a", "b", "c", "d"],
                    "correct_index": i % 4,
                }
                for i in range(10)
            ]
        }
    )


def _make_client() -> OllamaLLMClient:
    """Instancie le client en passant tous les paramètres → aucun accès à
    settings, donc pas de dépendance à la config Django dans ces tests."""
    return OllamaLLMClient(model="mistral:7b", host="http://localhost:11434", timeout=1)


def test_succes_premier_essai(monkeypatch):
    client = _make_client()
    calls = {"n": 0}

    def fake_call(_prompt):
        calls["n"] += 1
        return _valid_raw()

    monkeypatch.setattr(client, "_call_ollama", fake_call)

    quiz = client.generate_quiz("Un cours à réviser.", "Titre")
    assert len(quiz) == 10
    assert calls["n"] == 1  # aucun retry inutile


def test_retry_puis_succes(monkeypatch):
    """Deux réponses invalides, puis une valide : le retry sauve la génération."""
    client = _make_client()
    responses = ['{"questions": []}', "pas du json", _valid_raw()]
    calls = {"n": 0}

    def fake_call(_prompt):
        raw = responses[calls["n"]]
        calls["n"] += 1
        return raw

    monkeypatch.setattr(client, "_call_ollama", fake_call)

    quiz = client.generate_quiz("Un cours à réviser.", "Titre")
    assert len(quiz) == 10
    assert calls["n"] == 3  # a bien réessayé jusqu'à la réponse valide


def test_echec_apres_max_retries(monkeypatch):
    """Toujours invalide : LLMError levée après exactement MAX_RETRIES appels."""
    client = _make_client()
    calls = {"n": 0}

    def fake_call(_prompt):
        calls["n"] += 1
        return "toujours invalide"

    monkeypatch.setattr(client, "_call_ollama", fake_call)

    with pytest.raises(LLMError):
        client.generate_quiz("Un cours à réviser.", "Titre")
    assert calls["n"] == MAX_RETRIES
