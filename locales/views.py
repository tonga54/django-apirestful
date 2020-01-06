from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from locales.models import Local, LocalizacionLocal
from locales.serializer import LocalSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def show_list(request):
    if (request.method == "GET"):
        data = Local.objects.all()
        serializerLocal = LocalSerializer(data, many = True)
        return Response(serializerLocal.data)
    elif (request.method == "POST"):
        serializerLocal = LocalSerializer(data=request.data)
        if(serializerLocal.is_valid()):
            local = serializerLocal.create(request.data)
            return Response(serializerLocal.data, status = status.HTTP_201_CREATED)

        return Response(serializerLocal.errors, status = status.HTTP_400_BAD_REQUEST)