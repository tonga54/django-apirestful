from django.contrib import admin


# Register your models here.

# Hacer que este modelo sea accesible desde el panel de admin
from .models import Trabajador, Rol, Cliente, Usuario, Estado, AtencionClienteEmpleadoLocal, AtencionClienteTrabajador, Valoracion

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ()

class TrabajadorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class RolAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class EstadoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AtencionClienteTrabajadorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AtencionClienteEmpleadoLocalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ValoracionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Estado, EstadoAdmin)
admin.site.register(AtencionClienteTrabajador, AtencionClienteTrabajadorAdmin)
admin.site.register(AtencionClienteEmpleadoLocal, AtencionClienteEmpleadoLocalAdmin)
admin.site.register(Valoracion, ValoracionAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Cliente, ClienteAdmin)