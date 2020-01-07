from django.urls import path
from locales import views

urlpatterns = [
    path('', views.show_list, name="Page"),
    path('create', views.create, name="Page"),
]