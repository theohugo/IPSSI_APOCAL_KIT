"""URLs racine du projet APOCAL'IPSSI."""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


def health(_request):
    """Endpoint trivial pour les healthchecks externes."""
    return JsonResponse({"status": "ok", "service": "apocal-backend"})


urlpatterns = [
    # Health
    path("health/", health, name="health"),

    # Admin Django (utile en dev)
    path("admin/", admin.site.urls),

    # API — apps métier
    path("api/accounts/", include("accounts.urls")),
    path("api/llm/",      include("llm.urls")),
    path("api/quizzes/",  include("quizzes.urls")),

    # OpenAPI schema + Swagger UI + Redoc
    path("api/schema/",     SpectacularAPIView.as_view(),       name="schema"),
    path("api/docs/",       SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("api/redoc/",      SpectacularRedocView.as_view(url_name="schema"),    name="redoc"),
]
