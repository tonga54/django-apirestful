from rest_framework import serializers
from servicios.serializers import ServicioSerializer
from locales.models import Local, LocalizacionLocal, LocalTrabajador, LocalTrabajadorServicio

class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalizacionLocal
        fields = ['id', 'lat', 'lng']

class LocalSerializer(serializers.ModelSerializer):
    localizacion = LocalizacionSerializer(many=False)
    
    class Meta:
        model = Local
        fields = ['id', 'razonSocial', 'telefono', 'rut', 'descripcion', 'localizacion']

class EliminarTrabajadorLocalSerializer(serializers.ModelSerializer):
    local_id = serializers.IntegerField(required=True)
    trabajador_id = serializers.IntegerField(required=True)

    class Meta:
        model = LocalTrabajador
        fields = ['local_id', 'trabajador_id']

class TrabajadorLocalSerializer(serializers.ModelSerializer):
    local_id = serializers.IntegerField(required=True)
    rol_id = serializers.IntegerField(required=True)
    trabajador_id = serializers.IntegerField(required=True)

    class Meta:
        model = LocalTrabajador
        fields = ['local_id', 'rol_id', 'trabajador_id']

class LocalTrabajadorServicio_CustomSerializer(serializers.ModelSerializer):
    servicio = serializers.IntegerField(required=True)
    precio = serializers.DecimalField(max_digits=8, decimal_places=4, required=True)
    duracion = serializers.DecimalField(max_digits=8, decimal_places=4, required=True)

    class Meta:
        model = LocalTrabajadorServicio
        fields = ['servicio', 'precio', 'duracion']

    
class LocalTrabajadorServicioSerializer(serializers.ModelSerializer):
    local_trabajador_id = serializers.IntegerField(required=True)
    serviciosVM = LocalTrabajadorServicio_CustomSerializer(many=True)

    class Meta:
        model = LocalTrabajadorServicio
        fields = ['local_trabajador_id', 'serviciosVM']


