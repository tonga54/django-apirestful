# MODELOS
from locales.models import Servicio

# DJANGO
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# SERIALIZER
from servicios.serializers import ServicioSerializer

class ServicioViewSet(viewsets.ViewSet):

    def list(self):
        queryset = Servicio.objects.all()
        serializer = ServicioSerializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        serializer = ServicioSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            result = Servicio.objects.get(id=pk)
            servicio = ServicioSerializer(result)
            return Response(servicio.data, status = status.HTTP_200_OK)
        except Servicio.DoesNotExist:
            return Response({"result":"No existe el servicio."}, status = status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        serializer = ServicioSerializer(data=request.data)
        if(serializer.is_valid()):
            local = Servicio.objects.filter(id=pk)
            if local is not None:
                local.update(**request.data)
                local = Servicio.objects.get(id=pk)
                serializer = ServicioSerializer(local)
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        servicio = Servicio.objects.filter(id=pk)
        if servicio is not None:
            servicio.delete()
            return Response({"result": "Servicio eliminado con exito."}, status = status.HTTP_200_OK)
        else:
            return Response({"result":"No existe el servicio."}, status = status.HTTP_204_NO_CONTENT)


    