from rest_framework import serializers
from locales.models import Local, LocalizacionLocal

class LocalSerializer(serializers.ModelSerializer):
    # lat = serializers.FloatField(LocalizacionLocal.lat)
    # lng = serializers.FloatField(LocalizacionLocal.lng)
    # icono = serializers.FloatField(LocalizacionLocal.icono)

    lat = serializers.FloatField()
    lng = serializers.FloatField()
    icono = serializers.FloatField()
    
    class Meta:
        model = Local
        fields = ['razonSocial', 'telefono', 'rut', 'descripcion', 'lat', 'lng', 'icono']

        def create(self):
            

            localizacion = LocalizacionLocal(
                lat =  self.validated_data['lat'],
                lng = self.validated_data['lng'],
                icono = self.validated_data['icono']
            )

            try:
                localizacion.save()    
                local = Local(
                    razonSocial = self.validated_data['razonSocial'],
                    telefono = self.validated_data['telefono'],
                    rut = self.validated_data['rut'],
                    descripcion = self.validated_data['descripcion'],
                    localizacion = localizacion
                )

                local.save()

            except:
                print("ERROR")


            return local