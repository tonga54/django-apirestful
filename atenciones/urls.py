from django.urls import path
from servicios import views

urlpatterns = [
    path('', views.list, name="Ver servicios"),
    path('create', views.create, name="Crear servicio"),
    path('retrieve/<int:pk>', views.retrieve, name="Traer un servicio"),
    path('update/<int:pk>', views.update, name="Actualizar servicio"),
    path('destroy/<int:pk>', views.destroy, name="Eliminar servicio"),
]