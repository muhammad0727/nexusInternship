from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'role', 'password']
        

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'role', 'bio', 'portfolio', 'id']
        read_only_fields = ['id', 'role', 'username']
        