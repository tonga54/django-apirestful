from django.contrib import admin


# Register your models here.

# Hacer que este modelo sea accesible desde el panel de admin
from .models import Local, LocalizacionLocal, LocalTrabajador, LocalTrabajadorServicio, ImagenLocal

class LocalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class LocalizacionLocalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ImagenLocalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class LocalTrabajadorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class LocalTrabajadorServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Local, LocalAdmin)
admin.site.register(LocalizacionLocal, LocalizacionLocalAdmin)
admin.site.register(ImagenLocal, LocalizacionLocalAdmin)
admin.site.register(LocalTrabajador, LocalTrabajadorAdmin)
admin.site.register(LocalTrabajadorServicio, LocalTrabajadorServicioAdmin)