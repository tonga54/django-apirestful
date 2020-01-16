# VIEWSET
from locales.viewsets import LocalViewSet, TrabajadorLocalViewSet

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
def list(request):
    if (request.method == "GET"):
        viewset = LocalViewSet()
        return viewset.list()
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    if (request.method == "POST"):
        viewset = LocalViewSet()
        return viewset.create(request)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def retrieve(request, pk):
    if (request.method == "POST"):
        viewset = LocalViewSet()
        return viewset.retrieve(request, pk)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update(request, pk):
    if (request.method == "PUT"):
        viewset = LocalViewSet()
        return viewset.update(request, pk)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

# @api_view(['PATCH'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def partial_update(request, pk):
#     if (request.method == "PATCH"):
#         viewset = LocalViewSet()
#         return viewset.partial_update(request, pk)
#     return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def destroy(request, pk):
    if (request.method == "DELETE"):
        viewset = LocalViewSet()
        return viewset.destroy(request, pk)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def asignar_servicio(request):
#     if (request.method == "POST"):
#         viewset = LocalViewSet(request)
#         return viewset.asignar_servicio(request)
#     return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def asignar_trabajador_local(request):
    if (request.method == "POST"):
        viewset = TrabajadorLocalViewSet()
        return viewset.asignar_trabajador_local(request)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def eliminar_trabajador_local(request):
    if (request.method == "DELETE"):
        viewset = TrabajadorLocalViewSet()
        return viewset.eliminar_trabajador_local(request)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def asignar_servicios_trabajador_local(request):
    if (request.method == "POST"):
        viewset = TrabajadorLocalViewSet()
        return viewset.asignar_servicios_trabajador_local(request)
    return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)