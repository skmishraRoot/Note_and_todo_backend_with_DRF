from rest_framework.response  import Response
from rest_framework.generics import CreateAPIView
from authapi.serializers import RegisterUserSerializer, MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import login

# Register user view
class RegisterUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

# user tokens view
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer