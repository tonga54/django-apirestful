from rest_framework import serializers
from locales.models import Local, LocalizacionLocal

class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalizacionLocal
        # fields = ['lat', 'lng', 'icono']
        fields = ['id', 'lat', 'lng']

class LocalSerializer(serializers.ModelSerializer):
    localizacion = LocalizacionSerializer(many=False)
    
    class Meta:
        model = Local
        fields = ['id', 'razonSocial', 'telefono', 'rut', 'descripcion', 'localizacion']