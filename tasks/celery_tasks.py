"""This is the celery configuration for the task."""
from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail

from .models import Task


@shared_task
def send_task_reminder():
    """This task sends reminders for tasks that are due soon."""
    now = datetime.now()
    reminder_time = now + timedelta(hours=1)
    tasks = Task.objects.filter(due_date__range=(now, reminder_time), status='pending')

    for task in tasks:
        subject = f"Reminder: Task '{task.title}' is due soon!"
        message = f"""
        Dear {task.assigned_user.username},
        
        Your task '{task.title}' is due on {task.due_date}.
        Please make sure to complete it on time.

        Regards,
        Task Management System
        """
        send_mail(subject, message, 'demo@gmail.com', ["abc@gmail.com"])
