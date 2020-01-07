from django.urls import path
from usuarios.views import registration, login

urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', login, name='login')
]