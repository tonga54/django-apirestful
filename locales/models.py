from django.db import models
# from usuarios.models import Trabajador, Rol
from usuarios.models import Rol, Trabajador
from servicios.models import Servicio

class LocalizacionLocal(models.Model):
    lat = models.FloatField(verbose_name="Latitud")
    lng = models.FloatField(verbose_name="Longitud")
    icono = models.ImageField(verbose_name="Icono", upload_to="iconos_locales", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Localizacion del local"
        verbose_name_plural = "Localizacion de los locales"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return self.lat



class Local(models.Model):
    razonSocial = models.CharField(max_length=100, verbose_name="Razon social")
    telefono = models.CharField(max_length=8, verbose_name="Telefono")
    rut = models.BigIntegerField(verbose_name="Rut")
    localizacion = models.OneToOneField(
        LocalizacionLocal, 
        on_delete=models.CASCADE, 
        primary_key=True, 
        related_name="Localizacion")
    descripcion = models.TextField(verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locales"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return self.razonSocial


class ImagenLocal(models.Model):
    foto = models.ImageField(verbose_name="Foto", upload_to="imagenes_locales", null=True, blank=True)
    local = models.ForeignKey('locales.Local', on_delete=models.CASCADE, related_name="ImagenLocal")
    alt = models.CharField(max_length=100, verbose_name="Alt")
    title = models.CharField(max_length=100, verbose_name="Titulo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")


    class Meta:
        verbose_name = "Imagen del local"
        verbose_name_plural = "Imagenes de los locales"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return self.title


class LocalTrabajador(models.Model):
    local = models.ForeignKey('locales.Local', on_delete=models.CASCADE, related_name="Local")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="Rol")
    trabajador = models.OneToOneField(
        Trabajador,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="Trabajador"
    )
    serviciosQuePuedeRealizar = models.ManyToManyField(Servicio, through='LocalTrabajadorServicio', related_name="LocalTrabajador")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")


    class Meta:
        verbose_name = "Empleado del local"
        verbose_name_plural = "Empleados del local"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return self.created


class LocalTrabajadorServicio(models.Model):
    localTrabajador = models.ForeignKey(LocalTrabajador, on_delete=models.CASCADE, related_name="Empleado")
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name="Servicio")
    precio = models.FloatField(verbose_name="Precio")
    duracion = models.FloatField(verbose_name="Duracion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Servicios que brinda el empleado del local"
        verbose_name_plural = "Servicios que brindan los empleados del local"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return self.precio
