from django.urls import path
from servicios import views

urlpatterns = [
    path('', views.show_list, name="Ver servicios"),
    path('create', views.create, name="Crear servicio"),
    path('update/<int:pk>', views.update, name="Actualizar servicio"),
    path('destroy/<int:pk>', views.destroy, name="Eliminar servicio"),
]