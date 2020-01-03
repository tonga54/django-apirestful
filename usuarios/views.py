from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# SERIALIZADORES
from usuarios.serializers import RegistrationSerializer

# LOGIN PERSONALIZADO
from usuarios.backends import EmailBackend

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            usuario = serializer.save()
            token, _ = Token.objects.get_or_create(user=usuario)
            data = {"token": token.key}
        else:
            data = serializer.errors
        return Response(data)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    # user = authenticate(email=email, password=password)
    user = EmailBackend().authenticate(username = email, password = password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'user' : user.email}, status=HTTP_200_OK)