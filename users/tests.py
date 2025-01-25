"""
Unit tests for the users module in the Task and Product Management system.

This module contains test cases for user-related functionalities.
"""

from datetime import datetime, timedelta
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category
from tasks.celery_tasks import send_task_reminder
from tasks.models import Task
from products.models import Product
User = get_user_model()


class AuthenticationTests(APITestCase):
    def setUp(self):
        """
        Set up the test environment for category tests.
        """
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.login_url = "/api/users/login/"

    def test_login(self):
        """
        Test the login functionality for a user.
        """
        data = {"username": "testuser", "password": "password123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


class CategoryTests(APITestCase):
    """
    Test cases for category-related functionalities.
    """

    def setUp(self):
        """
        Set up the test environment for category tests.
        """
        self.admin = User.objects.create_superuser(
            username="admin", password="password123"
        )
        response = self.client.post(
            "/api/users/login/", data={"username": "admin", "password": "password123"}
        )
        # Save the access token
        self.access_token = response.data["access"]

    def test_create_category(self):
        """Test the creation of new category."""
        data = {
            "name": "Clothes",
            "description": "This category is for the clothes",
            "is_active": True,
            "created_by": 2,
            "parent_category": 1,
        }
        response = self.client.post(
            "/api/category/", data, HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().name, "Electronics")


class TaskReminderTests(TestCase):
    """
    Test cases for task reminder functionalities.
    """

    @patch("tasks.celery_tasks.send_mail")
    def test_send_task_reminder(self, mock_send_mail):
        """
        Test the sending of task reminders.
        """
        User = get_user_model()
        user = User.objects.create_user(username="testuser", password="password123")
        category = Category.objects.create(name="Test Category", created_by=user)
        product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            category=category,
            created_by=user,
            price=10.99,
            stock=100,
            is_active=True
        )
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            status="pending",
            due_date=datetime.now() + timedelta(minutes=55),
            assigned_user=user,
            product=product,
        )
        send_task_reminder()
        mock_send_mail.assert_called_once()
