"""
Endpoints d'authentification :
    POST /api/accounts/signup/  — créer un compte
    POST /api/accounts/login/   — se connecter (renvoie un token)
    POST /api/accounts/logout/  — se déconnecter (invalide le token)
    GET  /api/accounts/me/      — renvoie l'utilisateur courant
"""
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, SignupSerializer, UserSerializer


class SignupView(APIView):
    """Inscription d'un nouvel utilisateur."""

    permission_classes = [AllowAny]

    @extend_schema(
        request=SignupSerializer,
        responses={201: UserSerializer},
        description="Crée un nouveau compte utilisateur.",
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """Connexion par username + password. Renvoie un token API + crée la session."""

    permission_classes = [AllowAny]

    @extend_schema(
        request=LoginSerializer,
        responses={200: OpenApiResponse(description="{ token, user }")},
        description="Authentifie l'utilisateur et renvoie un token DRF.",
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        # Crée (ou récupère) le token API
        token, _created = Token.objects.get_or_create(user=user)

        # Crée également une session Django (utile pour la Swagger UI)
        django_login(request, user)

        return Response({
            "token": token.key,
            "user":  UserSerializer(user).data,
        })


class LogoutView(APIView):
    """Déconnexion : invalide le token + détruit la session."""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={204: OpenApiResponse(description="Déconnexion réussie")},
        description="Invalide le token DRF de l'utilisateur courant et détruit la session.",
    )
    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        django_logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeView(APIView):
    """Renvoie l'utilisateur connecté (utile pour le front : restaurer la session)."""

    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200: UserSerializer})
    def get(self, request):
        return Response(UserSerializer(request.user).data)
