from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings

# Define user roles
class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('support', 'Support'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    
    
    





# Service Type Model
class ServiceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Request Status Model
class RequestStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


# Service Request Model
class ServiceRequest(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="service_requests")
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_type.name} - {self.status.status}"

