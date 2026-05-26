"""
Endpoints quizz :
    GET    /api/quizzes/         — historique des quizz du user connecté
    GET    /api/quizzes/<id>/    — détail d'un quiz (avec les 10 questions)
    POST   /api/quizzes/<id>/answer/ — soumission de réponses + correction (K2)

K1 fournit les endpoints en lecture. K2 enrichira avec la création depuis
LLM et l'évaluation des réponses.
"""
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Quiz
from .serializers import QuizSerializer, QuizSummarySerializer


class QuizListView(generics.ListAPIView):
    """Historique des quizz du user connecté."""

    serializer_class = QuizSummarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user).order_by("-created_at")

    @extend_schema(description="Liste paginée des quizz de l'utilisateur connecté.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class QuizDetailView(generics.RetrieveAPIView):
    """Détail d'un quiz (les 10 questions complètes)."""

    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Sécurité : un user ne peut voir que ses propres quizz
        return Quiz.objects.filter(user=self.request.user)
