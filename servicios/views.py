# CLASES DEL MODELO
from servicios.models import Servicio

# SERIALIZADORES
from .serializers import ServicioSerializer

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
        data = Servicio.objects.all()
        serializer = ServicioSerializer(data, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    if (request.method == "POST"):
        serializer = ServicioSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update(request, pk):
    if (request.method == "PUT"):
        serializer = ServicioSerializer(data=request.data)
        if(serializer.is_valid()):
            result = serializer.update(request.data, pk)
            if result is not None:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response({"result":"No existe el servicio."}, status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def destroy(request, pk):
    if (request.method == "DELETE"):
        serializer = ServicioSerializer()
        result = serializer.destroy(pk)
        if result is not None:
            return Response(result, status = status.HTTP_200_OK)
        else:
            return Response({"result":"No existe el servicio."}, status = status.HTTP_204_NO_CONTENT)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)