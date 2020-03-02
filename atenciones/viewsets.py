# MODELOS
from locales.models import Local, LocalizacionLocal, LocalTrabajador, Trabajador, LocalTrabajadorServicio, Rol, Servicio

# DJANGO
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# SERIALIZER
from locales.serializer import LocalSerializer, LocalizacionSerializer, TrabajadorLocalSerializer, LocalTrabajadorServicioSerializer, EliminarTrabajadorLocalSerializer

class LocalViewSet(viewsets.ViewSet):

    def list(self):
        queryset = Local.objects.all()
        serializer = LocalSerializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        serializer = LocalSerializer(data=request.data)
        if(serializer.is_valid()):
            localizacionData = request.data.pop('localizacion')
            localizacion = LocalizacionLocal.objects.create(**localizacionData)
            local = Local.objects.create(localizacion = localizacion, **request.data)
            serializer = LocalSerializer(local)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            result = Local.objects.get(id=pk)
            local = LocalSerializer(result)
            return Response(local.data, status = status.HTTP_200_OK)
        except Local.DoesNotExist:
            return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        serializer = LocalSerializer(data=request.data)
        if(serializer.is_valid()):
            local = Local.objects.filter(id=pk)
            if local is not None:
                localizacion = request.data.pop('localizacion')
                local.update(**request.data)
                local = Local.objects.get(id=pk)
                serializer = LocalSerializer(local)
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk=None):
    #     # request_data = CustomRequest.verificarParametros(request.data, self.fields_serializer_local)
    #     # if 'localizacion' in request_data :
    #     #     request_data['localizacion'] = CustomRequest.verificarParametros(request.data['localizacion'], self.fields_serializer_localizacion)
    #     request_data = request.data

    #     # Si el diccionario no esta vacio.
    #     # if request_data:
    #     serializer = LocalSerializer(data=request_data, partial = True)
    #     if(serializer.is_valid()):
    #         localizacion = request_data.pop('localizacion')
    #         result = Local.objects.filter(id=pk).update(**request_data)
    #         if result == 1:
    #             local = Local.objects.get(id=pk)
    #             LocalizacionLocal.objects.filter(id=local.localizacion.id).update(**localizacion)
    #             local = Local.objects.get(id=pk)
    #             serializer = LocalSerializer(local)
    #             return Response(serializer.data, status = status.HTTP_201_CREATED)
    #         return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)
    #     else:
    #         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #     # else:
    #     #     return Response({"result":"Debes enviar algun parametro."}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        local = Local.objects.filter(id=pk)
        if local is not None:
            local.delete()
            return Response({"result": "Local eliminado con exito."}, status = status.HTTP_200_OK)
        else:
            return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)


    # def asignar_servicio(self, request):

    #     new_track.file = request.FILES['file']
    #     new_track.save()

    #     new_store = Store.objects.get(id=int(request.POST['store']))
    #     new_track.store.add(new_store)


class TrabajadorLocalViewSet(viewsets.ViewSet):

    def asignar_trabajador_local(self, request):
        serializer = TrabajadorLocalSerializer(data = request.data)
        if(serializer.is_valid()):
            try:
                local = Local.objects.get(id=request.data['local_id'])
                rol = Rol.objects.get(id=request.data['rol_id'])
                trabajador = Trabajador.objects.get(id=request.data['trabajador_id'])

                result = LocalTrabajador(local = local, rol = rol, trabajador = trabajador)
                result.save()
                serializer = TrabajadorLocalSerializer(result)
                return Response(serializer.data, status = status.HTTP_201_CREATED)

            except Local.DoesNotExist:
                return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)
            except Rol.DoesNotExist:
                return Response({"result":"No existe el rol."}, status = status.HTTP_204_NO_CONTENT)
            except Trabajador.DoesNotExist:
                return Response({"result":"No existe el trabajador."}, status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors)

    def eliminar_trabajador_local(self, request):
        serializer = EliminarTrabajadorLocalSerializer(data = request.data)
        if(serializer.is_valid()):
            try:
                local = Local.objects.get(id=request.data['local_id'])
                trabajador = Trabajador.objects.get(id=request.data['trabajador_id'])
                lt = LocalTrabajador.objects.get(local = local, trabajador = trabajador)
                servicios_locales_trabajadores = LocalTrabajadorServicio.objects.filter(localTrabajador = lt).delete()
                lt.delete()

                return Response({"result":"Trabajador eliminado del local."}, status = status.HTTP_200_OK)
            except Local.DoesNotExist:
                return Response({"result":"No existe el local."}, status = status.HTTP_204_NO_CONTENT)
            except Trabajador.DoesNotExist:
                return Response({"result":"No existe el trabajador."}, status = status.HTTP_204_NO_CONTENT)
            except LocalTrabajador.DoesNotExist:
                return Response({"result":"No existe ningun local con el trabajador asigando."}, status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors)


    def asignar_servicios_trabajador_local(self, request):
        serializer = LocalTrabajadorServicioSerializer(data = request.data)
        if(serializer.is_valid()):
            try:
                local_trabajador = LocalTrabajador.objects.get(id=request.data['local_trabajador_id'])
                listaServicios = []
                if isinstance(request.data['serviciosVM'], list):
                    if len(request.data['serviciosVM']) > 0:
                        for servicio in request.data['serviciosVM']:
                            servicioObject = {
                                "servicio": Servicio.objects.get(id = servicio['servicio']),
                                "precio": servicio['precio'],
                                "duracion" : servicio['duracion']
                            }
                            listaServicios.append(servicioObject)
                
                if len(listaServicios) > 0:
                    for serv in listaServicios:
                        obj = LocalTrabajadorServicio(
                                localTrabajador = local_trabajador, 
                                servicio = serv['servicio'],
                                precio = serv['precio'],
                                duracion = serv['duracion']
                            )
                        obj.save()

                return Response({"result":"Servicios asociados al trabajador con exito."}, status = status.HTTP_201_CREATED)

            except LocalTrabajador.DoesNotExist:
                return Response({"result":"No existe un usuario asociado a el local."}, status = status.HTTP_204_NO_CONTENT)
            except Servicio.DoesNotExist:
                return Response({"result":"No existe el servicio."}, status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors)
