from rest_framework import serializers
from .models import User


class RegisUserSerializer(serializers.ModelSerializer):
    """Serializer for creating new user instances."""
    username = serializers.CharField()
    nickname = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'nickname', 'password']

    def create(self, validated_data):
        """
        "create" method creates a new user instance using the provided data,
        and sets the user's password using the `set_password` method.
        """
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user