from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        # - indica al reves, es decir que ordene al reves
        ordering = ["-created"] 
    
    def __str__(self):
        return self.nombre