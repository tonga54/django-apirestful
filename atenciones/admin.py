from django.contrib import admin

# Register your models here.
from .models import Estado, AtencionClienteTrabajador, AtencionClienteEmpleadoLocal, Valoracion

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