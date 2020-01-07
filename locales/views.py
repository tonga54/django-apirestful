# CLASES DEL MODELO
from locales.models import Local, LocalizacionLocal

# SERIALIZADORES
from locales.serializer import LocalSerializer

# RENDER DE DJANGO
from django.shortcuts import render

# APPS DE RESTFRAMEWORK
from rest_framework.response import Response
from rest_framework import status
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
def show_list(request):
    if (request.method == "GET"):
        data = Local.objects.all()
        serializerLocal = LocalSerializer(data, many = True)
        return Response(serializerLocal.data)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    if (request.method == "POST"):
        serializerLocal = LocalSerializer(data=request.data)
        if(serializerLocal.is_valid()):
            local = serializerLocal.create(request.data)
            return Response(serializerLocal.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializerLocal.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)
    

        