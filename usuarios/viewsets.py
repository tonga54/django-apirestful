# MODELOS
from usuarios.models import Usuario, Trabajador, Cliente

# MODELO LOGIN PERSONALIZADO
from usuarios.backends import EmailBackend

import time

# DJANGO
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# DJANGO REST FRAMEWORK
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

# SERIALIZER
from usuarios.serializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ViewSet):
    fields_serializer_usuario = UsuarioSerializer.Meta.fields
    # fields_serializer_localizacion = LocalizacionSerializer.Meta.fields

    # def list(self):
    #     queryset = Local.objects.all()
    #     serializer = LocalSerializer(queryset, many = True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if(serializer.is_valid()):
            request.data['password'] = make_password(request.data['password'])
            request.data['username'] = int(time.time())
            usuario = Usuario.objects.create(**request.data)
            token, _ = Token.objects.get_or_create(user=usuario)
            # return Response(serializer.data, status = status.HTTP_201_CREATED)
            data = {"token": token.key}
            return Response(data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     try:
    #         result = Local.objects.get(id=pk)
    #         local = LocalSerializer(result)
    #         return Response(local.data, status = status.HTTP_200_OK)
    #     except Local.DoesNotExist:
    #         return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)

    # def update(self, request, pk=None):
    #     request_data = CustomRequest.verificarParametros(request.data, self.fields_serializer_local)
        
    #     if 'localizacion' in request.data:
    #         request_data['localizacion'] = CustomRequest.verificarParametros(request.data['localizacion'], self.fields_serializer_localizacion)

    #     if request_data:
    #         serializer = LocalSerializer(data=request_data)
    #         if(serializer.is_valid()):
    #             local = Local.objects.filter(id=pk)
    #             if local is not None:
    #                 localizacion = request_data.pop('localizacion')
    #                 local.update(**request_data)
    #                 local = Local.objects.get(id=pk)
    #                 serializer = LocalSerializer(local)
    #                 return Response(serializer.data, status = status.HTTP_201_CREATED)
    #             else:
    #                 return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)
    #         else:
    #             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response({"result":"Debes enviar los parametros requeridos."}, status = status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk=None):
    #     request_data = CustomRequest.verificarParametros(request.data, self.fields_serializer_local)
    #     if 'localizacion' in request_data :
    #         request_data['localizacion'] = CustomRequest.verificarParametros(request.data['localizacion'], self.fields_serializer_localizacion)

    #     # Si el diccionario no esta vacio.
    #     if request_data:
    #         serializer = LocalSerializer(data=request_data, partial = True)
    #         if(serializer.is_valid()):
    #             localizacion = request_data.pop('localizacion')
    #             result = Local.objects.filter(id=pk).update(**request_data)
    #             if result == 1:
    #                 local = Local.objects.get(id=pk)
    #                 LocalizacionLocal.objects.filter(id=local.localizacion.id).update(**localizacion)
    #                 local = Local.objects.get(id=pk)
    #                 serializer = LocalSerializer(local)
    #                 return Response(serializer.data, status = status.HTTP_201_CREATED)
    #             return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)
    #         else:
    #             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response({"result":"Debes enviar algun parametro."}, status = status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     local = Local.objects.filter(id=pk)
    #     if local is not None:
    #         local.delete()
    #         return Response({"result": "Servicio eliminado con exito."}, status = status.HTTP_200_OK)
    #     else:
    #         return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)


    # def asignar_servicio(self):
    #     new_track.file = request.FILES['file']
    #     new_track.save()

    #     new_store = Store.objects.get(id=int(request.POST['store']))
    #     new_track.store.add(new_store)

    def login(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response({'error': 'Por favor provenga de email y password.'}, status=status.HTTP_400_BAD_REQUEST)
        user = EmailBackend().authenticate(username = email, password = password)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user' : user.email}, status=status.HTTP_200_OK)

    # def registrarTrabajador(self, request, pk):
        