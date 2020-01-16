from rest_framework import serializers
from usuarios.models import Usuario, Cliente, Trabajador


class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ['id', 'password', 'email', 'first_name', 'last_name', 'telefono']

class TrabajadorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(many=False)

    class Meta:
        model = Trabajador
        fields = ['id', 'usuario', 'descripcion', 'aDomicilio']

class ClienteSerializer(serializers.ModelSerializer):
    # usuario = UsuarioSerializer(many=False)
    
    class Meta:
        model = Cliente
        fields = ['id', 'usuario']