"""This module contains views functionaliy for the users."""

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from config import env_config
from users.api.serializer import (
    ForgotPasswordSerializer,
    RegisterSerializer,
    ResetPasswordSerializer,
)
from utils import message

User = get_user_model()


class RegisterView(APIView):
    """This class implements the registration of a user"""

    permission_classes = [AllowAny]

    def post(self, request):
        """This method is used to register a user."""
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(APIView):
    """View to send a password reset email."""

    def post(self, request):
        """This method is used to send a reset email"""
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            user = User.objects.get(email=email)

            # Generate a token for password reset
            token = default_token_generator.make_token(user)

            # Send the reset link to the user's email
            reset_link = f"{env_config.RESET_PWD_LINK_URL}{token}/"
            send_mail(
                "Password Reset",
                f"Click here to reset your password: {reset_link}",
                env_config.SENDER_EMAIL,
                [email],
            )

            return Response(
                {"message": message.PWD_EMAIL_SENT}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    """View to reset a user's password using the token."""

    def post(self, request):
        """This method is called to reset the password."""
        # Retrieve the user based on the token
        try:
            user = User.objects.get(id=request.data.get("user_id"))
        except User.DoesNotExist:
            return Response(
                {"error": message.USER_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ResetPasswordSerializer(
            data=request.data, context={"user_id": user.id}
        )
        if serializer.is_valid():
            new_password = serializer.validated_data["new_password"]
            user.set_password(new_password)
            user.save()
            return Response(
                {"message": message.PWD_RESET_SUCCESS}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
