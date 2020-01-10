# MODELOS
from django.contrib.auth.models import User
from locales.models import Local, LocalizacionLocal

# DJANGO
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from custom.request import CustomRequest

# SERIALIZER
from locales.serializer import LocalSerializer, LocalizacionSerializer

class LocalViewSet(viewsets.ViewSet):
    serializer_class = LocalSerializer
    fields_serializer_local = LocalSerializer.Meta.fields
    fields_serializer_localizacion = LocalizacionSerializer.Meta.fields

    def list(self):
        queryset = Local.objects.all()
        serializer = LocalSerializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        request_data = CustomRequest.verificarParametros(request.data, self.fields_serializer_local)
        request_data['localizacion'] = CustomRequest.verificarParametros(request.data['localizacion'], self.fields_serializer_localizacion)
        if request_data:
            serializer = LocalSerializer(data=request.data)
            if(serializer.is_valid()):
                localizacionData = request_data.pop('localizacion')
                localizacion = LocalizacionLocal.objects.create(**localizacionData)
                local = Local.objects.create(localizacion = localizacion, **request_data)
                serializer = LocalSerializer(local)
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"result":"Debes enviar los parametros requeridos."}, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        result = Local.objects.get(id=pk)
        if result is not None:
            local = LocalSerializer(result)
            return Response(local.data, status = status.HTTP_200_OK)
        else:
            return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        request_data = CustomRequest.verificarParametros(request.data, self.fields_serializer_local)
        request_data['localizacion'] = CustomRequest.verificarParametros(request.data['localizacion'], self.fields_serializer_localizacion)

        if request_data:
            serializer = LocalSerializer(data=request_data)
            if(serializer.is_valid()):
                local = Local.objects.filter(id=pk)
                if local is not None:
                    localizacion = request_data.pop('localizacion')
                    local.update(**request_data)
                    local = Local.objects.get(id=pk)
                    serializer = LocalSerializer(local)
                    return Response(serializer.data, status = status.HTTP_201_CREATED)
                else:
                    return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"result":"Debes enviar los parametros requeridos."}, status = status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        request_data = CustomRequest.verificarParametros(request.data, self.fields_serializer_local)
        if 'localizacion' in request_data :
            request_data['localizacion'] = CustomRequest.verificarParametros(request.data['localizacion'], self.fields_serializer_localizacion)

        # Si el diccionario no esta vacio.
        if request_data:
            serializer = LocalSerializer(data=request_data, partial = True)
            if(serializer.is_valid()):
                localizacion = request_data.pop('localizacion')
                result = Local.objects.filter(id=pk).update(**request_data)
                if result == 1:
                    local = Local.objects.get(id=pk)
                    LocalizacionLocal.objects.filter(id=local.localizacion.id).update(**localizacion)
                    local = Local.objects.get(id=pk)
                    serializer = LocalSerializer(local)
                    return Response(serializer.data, status = status.HTTP_201_CREATED)
                return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"result":"Debes enviar algun parametro."}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        local = Local.objects.filter(id=pk)
        if local is not None:
            local.delete()
            return Response({"result": "Servicio eliminado con exito."}, status = status.HTTP_200_OK)
        else:
            return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)


    