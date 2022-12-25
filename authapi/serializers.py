# Importing models 
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




# Making serializer for Registering a User
class RegisterUserSerializer(serializers.ModelSerializer):
    # Defining some extra things for these fields
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True,validators=[validate_password])

    # Defining fields and model
    class Meta:
        model = User
        fields = ['username','password','email', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    # Creating user in the database
    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'],
            email=validate_data['email'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name'],
        )

        user.set_password(validate_data['password'])
        user.save()
        return user




# Serializer for token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token