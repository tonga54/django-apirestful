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
        local = Local.objects.create(**validated_data)
        LocalizacionLocal.objects.create(local=local, **localizacionData)
        return local