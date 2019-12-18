from django.urls import path
from servicios import views


urlpatterns = [
    path('', views.show_list, name="Page")
]