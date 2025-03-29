from django.contrib.auth.models import AbstractUser
from django.db import models

# Define user roles
class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('support', 'Support'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
