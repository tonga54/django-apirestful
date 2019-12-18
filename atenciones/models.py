# from django.db import models
# from usuarios.models import Trabajador, TrabajadorServicio, Cliente
# from locales.models import Local, LocalTrabajador, LocalTrabajadorServicio


# class Estado(models.Model):
#     nombre = models.CharField(max_length=128, verbose_name="Estado")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

#     class Meta:
#         verbose_name = "Estado"
#         verbose_name_plural = "Estados"
#         ordering = ["-created"] 
    
#     def __str__(self):
#         return self.nombre
        
# class AtencionClienteTrabajador(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="atencion_cliente")
#     trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name="atecion_trabajador")
#     costoDiferencial = models.FloatField(verbose_name="Costo diferencial")
#     fechaHoraReserva = models.DateTimeField(verbose_name="Fecha y hora reserva")
#     timestampComienzo = models.DateTimeField(verbose_name="Hora de comienzo/llegada")
#     timestampFinalizado = models.DateTimeField(verbose_name="Hora de finalizacion")
#     servicio = models.ForeignKey(TrabajadorServicio, on_delete=models.CASCADE, related_name="trabajador_servicio_cliente")
#     estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

#     class Meta:
#         verbose_name = "Localizacion local"
#         verbose_name_plural = "Localizacion locales"
#         # - indica al reves, es decir que ordene al reves
#         ordering = ["-created"] 
    
#     def __str__(self):
#         return self.fechaHoraReserva


# class AtencionClienteEmpleadoLocal(models.Model):
#     local = models.ForeignKey(Local, on_delete=models.CASCADE, related_name="atencion_cliente_empleado_local")
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="atencion_cliente")
#     trabajador = models.ForeignKey(LocalTrabajador, on_delete=models.CASCADE, related_name="atencion_cliente_empleado_local_trabajador")
#     servicio = models.ForeignKey(LocalTrabajadorServicio, on_delete=models.CASCADE, related_name="atencion_cliente_empleado_local_trabajador_servicio")
#     costoDiferencial = models.FloatField(verbose_name="Costo diferencial")
#     fechaHoraReserva = models.DateTimeField(verbose_name="Fecha y hora reserva")
#     timestampComienzo = models.DateTimeField(verbose_name="Hora de comienzo/llegada")
#     timestampFinalizado = models.DateTimeField(verbose_name="Hora de finalizacion")
#     servicio = models.ForeignKey(TrabajadorServicio, on_delete=models.CASCADE, related_name="trabajador_servicio_local_trabajador_servicio")
#     estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

#     class Meta:
#         verbose_name = "Localizacion local"
#         verbose_name_plural = "Localizacion locales"
#         # - indica al reves, es decir que ordene al reves
#         ordering = ["-created"] 
    
#     def __str__(self):
#         return self.fechaHoraReserva

# class Valoracion(models.Model):
#     descripcion = models.TextField(verbose_name="Descripcion")
#     puntuacion = models.FloatField(verbose_name="Puntuacion")
#     AtencionClienteTrabajador = models.ForeignKey(AtencionClienteTrabajador, on_delete=models.CASCADE, related_name="atencion_cliente_trabajador")
#     AtencionClienteEmpleadoLocal = models.ForeignKey(AtencionClienteEmpleadoLocal, on_delete=models.CASCADE, related_name="atencion_cliente_empleado_local")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

#     class Meta:
#         verbose_name = "Valoracion"
#         verbose_name_plural = "Valoraciones"
#         ordering = ["-created"] 
    
#     def __str__(self):
#         return self.descripcion