from django.urls import path
from locales import views

urlpatterns = [
    path('', views.list, name="Page"),
    path('create', views.create, name="Page"),
    path('retrieve/<int:pk>', views.retrieve, name="Traer un local"),
    path('update/<int:pk>', views.update, name="Actualizar local"),
    path('partial/<int:pk>', views.partial_update, name="Actualizar parcial un local"),
    path('destroy/<int:pk>', views.destroy, name="Eliminar local"),
]