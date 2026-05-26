"""
Endpoints LLM — K1 fournit /api/llm/ping/ uniquement.
K2 ajoutera /api/llm/generate-quiz/.

Le ping appelle réellement Ollama (si LLM_BACKEND="ollama") pour vérifier
que tout est correctement câblé.
"""
import requests
from django.conf import settings
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class PingView(APIView):
    """Vérifie que le backend voit Ollama (ou que le mock répond)."""

    permission_classes = [AllowAny]

    @extend_schema(
        responses={200: OpenApiResponse(description="{ backend, model, ollama_alive, message }")},
        description="Ping LLM — utile pour vérifier l'intégration Ollama.",
    )
    def get(self, _request):
        backend = settings.LLM_BACKEND

        if backend == "mock":
            return Response({
                "backend":      "mock",
                "model":        "mock-model",
                "ollama_alive": False,
                "message":      "Mock LLM actif (configurer LLM_BACKEND=ollama pour utiliser Ollama).",
            })

        # Mode Ollama : on tente un appel léger à /api/tags pour lister les modèles
        try:
            resp = requests.get(f"{settings.OLLAMA_HOST}/api/tags", timeout=2)
            resp.raise_for_status()
            tags = resp.json().get("models", [])
            model_present = any(m.get("name", "").startswith(settings.OLLAMA_MODEL.split(":")[0]) for m in tags)
            return Response({
                "backend":      "ollama",
                "model":        settings.OLLAMA_MODEL,
                "ollama_alive": True,
                "model_loaded": model_present,
                "message":      (
                    "Ollama répond ✓" if model_present
                    else f"Ollama répond mais le modèle {settings.OLLAMA_MODEL} n'est pas téléchargé. "
                         "Lancez : make pull-model"
                ),
            })
        except requests.RequestException as exc:
            return Response(
                {
                    "backend":      "ollama",
                    "model":        settings.OLLAMA_MODEL,
                    "ollama_alive": False,
                    "message":      f"Ollama injoignable : {exc}",
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
