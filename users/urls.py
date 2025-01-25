
"""This module contains the urls for the users app."""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.api.api_view import RegisterView, ResetPasswordView, ForgotPasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
]

