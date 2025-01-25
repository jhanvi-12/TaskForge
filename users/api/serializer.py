"""This module contains serializer information for users"""

from rest_framework import serializers

from django.contrib.auth import get_user_model
from utils import constant
from django.contrib.auth.tokens import default_token_generator
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User serializer class"""

    class Meta:
        """Meta class for user serializer"""

        model = User
        fields = ["id", "username", "email", "is_admin"]
        extra_kwargs = {"is_admin": {"read_only": True}}


class RegisterSerializer(serializers.ModelSerializer):
    """This class implements the registration serializer"""

    password = serializers.CharField(write_only=constant.STATUS_TRUE, min_length=8)

    class Meta:
        """Meta class for the register serializer"""

        model = User
        fields = ["id", "username", "email", "password", "is_admin"]

    def create(self, validated_data):
        """Method to create a new instance of the user."""
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        """Check if the email exists."""
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email not found.")
        return value

class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8)

    def validate_token(self, value):
        """Validate if the token is correct."""
        try:
            user = User.objects.get(id=self.context['user_id'])
            if not default_token_generator.check_token(user, value):
                raise serializers.ValidationError("Invalid token.")
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        return value