from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class RegisUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=2, max_length=50)
    nickname = serializers.CharField(min_length=3, max_length=60)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'nickname', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=2, max_length=50)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["username", "password"]

    def validated(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        return serializers.ValidationError("Такого пользователя нет")