from django.urls import path

from .views import PingView

urlpatterns = [
    path("ping/", PingView.as_view(), name="llm-ping"),
    # K2 ajoutera :
    # path("generate-quiz/", GenerateQuizView.as_view(), name="llm-generate-quiz"),
]
