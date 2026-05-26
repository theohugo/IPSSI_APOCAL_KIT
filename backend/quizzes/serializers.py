"""Sérialiseurs pour Quiz et Question."""
from rest_framework import serializers

from .models import Question, Quiz


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["index", "prompt", "options", "correct_index"]


class QuizSerializer(serializers.ModelSerializer):
    """Renvoie un quiz complet avec ses 10 questions."""

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "source_text", "score", "created_at", "questions"]
        read_only_fields = ["id", "created_at"]


class QuizSummarySerializer(serializers.ModelSerializer):
    """Version compacte pour la liste d'historique."""

    nb_questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ["id", "title", "score", "nb_questions", "created_at"]

    def get_nb_questions(self, obj: Quiz) -> int:
        return obj.questions.count()
