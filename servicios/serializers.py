from rest_framework import serializers
from servicios.models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'nombre']

    def update(self, validated_data, pk = None):
        servicio = Servicio.objects.filter(id=pk)
        if servicio is not None:
            servicio.update(**validated_data)
            return servicio
        else:
            return None

    def destroy(self, pk = None):
        servicio = Servicio.objects.filter(id=pk)
        if servicio is not None:
            servicio.delete()
            return {"result": "Servicio eliminado con exito."}
        else:
            return None
    
    def retrieve(self, validated_data, pk = None):
        return None

    def partialUpdate(self, validated_data, pk = None):
        return None
