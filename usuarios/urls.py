from django.urls import path
from usuarios import views

urlpatterns = [
    path('register', views.create, name='Registro'),
    path('login', views.login, name="Login"),
]