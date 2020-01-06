from django.urls import path
from servicios import views

urlpatterns = [
    path('', views.getServicios, name="Ver servicios"),
    path('create', views.createServicios, name="Crear servicios")
]