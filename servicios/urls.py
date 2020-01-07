from django.urls import path
from servicios import views

urlpatterns = [
    path('', views.show_list, name="Ver servicios"),
    path('create', views.create, name="Crear servicios")
]