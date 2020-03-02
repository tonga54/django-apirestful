from django.urls import path
from locales import views

urlpatterns = [
    path('', views.list, name="Page"),
    path('create', views.create, name="Page"),
    path('retrieve/<int:pk>', views.retrieve, name="Traer un local"),
    path('update/<int:pk>', views.update, name="Actualizar local"),
    # path('partial/<int:pk>', views.partial_update, name="Actualizar parcial un local"),
    path('destroy/<int:pk>', views.destroy, name="Eliminar local"),
    # path('asignarServicio', views.asignar_servicio, name="Asignar servicio a local"),
    path('asignarTrabajadorLocal', views.asignar_trabajador_local, name="Asignar trabajador a local"),
    path('eliminarTrabajadorLocal', views.eliminar_trabajador_local, name="Eliminar trabajador a local"),
    path('asignarServiciosTrabajadorLocal', views.asignar_servicios_trabajador_local, name="Asignar servicios a trabajador local"),
    path('modificarServicioTrabajadorLocal', views.modificar_servicio_trabajador_local, name="Asignar servicios a trabajador local")
]