from rest_framework import serializers
from locales.models import Local, LocalizacionLocal

class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalizacionLocal
        # fields = ['lat', 'lng', 'icono']
        fields = ['lat', 'lng']

class LocalSerializer(serializers.ModelSerializer):
    localizacion = LocalizacionSerializer(many=False)

    class Meta:
        model = Local
        fields = ['razonSocial', 'telefono', 'rut', 'descripcion', 'localizacion']
    
    def create(self, validated_data):
        localizacionData = validated_data.pop('localizacion')
        localizacion = LocalizacionLocal.objects.create(**localizacionData)
        local = Local.objects.create(localizacion = localizacion, **validated_data)
        return local