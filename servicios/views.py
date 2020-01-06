# CLASES DEL MODELO
from servicios.models import Servicio
from .serializers import ServicioSerializer

# RENDER DE DJANGO
from django.shortcuts import render

# APPS DE RESTFRAMEWORK
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# AUTENTICACION
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# DECORADORES
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view

@api_view(['GET'])
def getServicios(request):
    if (request.method == "GET"):
        data = Servicio.objects.all()
        serializer = ServicioSerializer(data, many = True)
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def createServicios(request):
    if (request.method == "POST"):
        serializer = ServicioSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_400_BAD_REQUEST)