from rest_framework import serializers
from usuarios.models import Usuario, Cliente


class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = '__all__'

        def save(self):
            usuario = Cliente(
                email = self.validated_data['data'],
                username = self.validated_data['username'],
                password = self.validated_data['password']
            )

            usuario = Cliente.objects.get_or_create(usuario=usuario)
            # usuario.save()

            return usuario