# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from servicios.models import Servicio
# from locales.models import Local
# from atenciones.models import AtencionClienteEmpleadoLocal, AtencionClienteTrabajador

class Usuario(AbstractUser):
    pass
    nombre = models.CharField(max_length=64, verbose_name="Nombre")
    apellido = models.CharField(max_length=64, verbose_name="Apellido")
    fotoPerfil = models.ImageField(verbose_name="Foto perfil", upload_to="fotos_perfil_usuario", null=True, blank=True)
    telefono = models.CharField(max_length=8, verbose_name="Telefono")


class Trabajador(models.Model):
    descripcion = models.CharField(max_length=256, verbose_name="Descripcion")
    aDomicilio = models.BooleanField(verbose_name="Trabaja a domicilio")
    servicios = models.ManyToManyField(Servicio, through='TrabajadorServicio', related_name="trabajador_servicio")
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="trabajador_usuario"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return self.descripcion

    
class Cliente(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="trabajador_cliente"
    )
    atencionClienteTrabajador = models.ManyToManyField(Trabajador, through='AtencionClienteTrabajador', related_name="atencion_cliente_trabajador")
    atencionClienteEmpleadoLocal = models.ManyToManyField('locales.local', through='AtencionClienteEmpleadoLocal', related_name="tb_cliente_atencion_cliente_empleado_local")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return "test"

class TrabajadorServicio(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name="trabajador_servicio")
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name="servicio_trabajador")
    precio = models.FloatField(verbose_name="Precio")
    duracion = models.TimeField(verbose_name="Duracion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
            verbose_name = "Trabajador servicio"
            verbose_name_plural = "Trabajadores servicios"
            # - indica al reves, es decir que ordene al reves
            ordering = ["-created"] 
        
    def __str__(self):
        return self.precio
    
class Rol(models.Model):
    nombre = models.CharField(max_length=32, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
            verbose_name = "Rol"
            verbose_name_plural = "Roles"
            # - indica al reves, es decir que ordene al reves
            ordering = ["-created"] 
        
    def __str__(self):
        return self.nombre



class Estado(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Estado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["-created"] 
    
    def __str__(self):
        return self.nombre
        
class AtencionClienteTrabajador(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="atencion_cliente_trabajador_tb_atencion_cliente")
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name="atecion_trabajador")
    costoDiferencial = models.FloatField(verbose_name="Costo diferencial")
    fechaHoraReserva = models.DateTimeField(verbose_name="Fecha y hora reserva")
    timestampComienzo = models.DateTimeField(verbose_name="Hora de comienzo/llegada")
    timestampFinalizado = models.DateTimeField(verbose_name="Hora de finalizacion")
    servicio = models.ForeignKey(TrabajadorServicio, on_delete=models.CASCADE, related_name="trabajador_servicio_cliente")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="atecion_cliente_trabajador_estado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Atencion del cliente con el trabajador independiente"
        verbose_name_plural = "Atencion de los clientes con los trabajadores independientes"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return self.fechaHoraReserva


class AtencionClienteEmpleadoLocal(models.Model):
    local = models.ForeignKey('locales.Local', on_delete=models.CASCADE, related_name="atencion_cliente_empleado_local")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="atencion_cliente_empleado_local_tb_atencion_cliente")
    trabajador = models.ForeignKey('locales.LocalTrabajador', on_delete=models.CASCADE, related_name="atencion_cliente_empleado_local_trabajador")
    servicio = models.ForeignKey('locales.LocalTrabajadorServicio', on_delete=models.CASCADE, related_name="atencion_cliente_empleado_local_trabajador_servicio")
    costoDiferencial = models.FloatField(verbose_name="Costo diferencial")
    fechaHoraReserva = models.DateTimeField(verbose_name="Fecha y hora reserva")
    timestampComienzo = models.DateTimeField(verbose_name="Hora de comienzo/llegada")
    timestampFinalizado = models.DateTimeField(verbose_name="Hora de finalizacion")
    servicio = models.ForeignKey(TrabajadorServicio, on_delete=models.CASCADE, related_name="trabajador_servicio_local_trabajador_servicio")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="atencion_cliente_empleado_local_estado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Atencion del cliente con el empleado en el local"
        verbose_name_plural = "Atenciones de los clientes con los empleados en el local"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return self.fechaHoraReserva

class Valoracion(models.Model):
    descripcion = models.TextField(verbose_name="Descripcion")
    puntuacion = models.FloatField(verbose_name="Puntuacion")
    AtencionClienteTrabajador = models.ForeignKey(AtencionClienteTrabajador, on_delete=models.CASCADE, related_name="atencion_cliente_trabajador")
    AtencionClienteEmpleadoLocal = models.ForeignKey(AtencionClienteEmpleadoLocal, on_delete=models.CASCADE, related_name="valoracion_tb_atencion_cliente_empleado_local")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Valoracion"
        verbose_name_plural = "Valoraciones"
        ordering = ["-created"] 
    
    def __str__(self):
        return self.descripcion