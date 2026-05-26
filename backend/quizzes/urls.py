from django.urls import path

from .views import QuizDetailView, QuizListView

urlpatterns = [
    path("",         QuizListView.as_view(),   name="quiz-list"),
    path("<int:pk>/", QuizDetailView.as_view(), name="quiz-detail"),
    # K2 ajoutera :
    # path("<int:pk>/answer/", AnswerQuizView.as_view(), name="quiz-answer"),
]
