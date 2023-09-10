from rest_framework import serializers, exceptions
from .models import  Pets
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password


class PetsSerializers(serializers.ModelSerializer):   
    class Meta:
        model = Pets
        fields = ['id', 'pets_name', 'content']
#sadasdasd
    def add(self, validated_data):
        return Pets.objects.add(**validated_data)
    
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})   

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')
        extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True}}

    def validate(self, attrs):
        print(attrs)
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise exceptions.ValidationError({"password2":["can't be another value than password field"]})
        return super().validate(attrs)

    # def validate_password(self, value:str) -> str:
    #     return make_password(value)
