# SERIALIZADORES
from usuarios.viewsets import UsuarioViewSet

# RENDER DE DJANGO
from django.shortcuts import render

# APPS DE RESTFRAMEWORK
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny

# AUTENTICACION
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# DECORADORES
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create(request):
    if request.method == 'POST':
        viewset = UsuarioViewSet()
        return viewset.create(request)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    if request.method == 'POST':
        viewset = UsuarioViewSet()
        return viewset.login(request)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)