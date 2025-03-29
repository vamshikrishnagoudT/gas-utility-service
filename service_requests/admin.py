from django.contrib import admin
from .models import ServiceRequest, ServiceType, RequestStatus

admin.site.register(ServiceRequest)
admin.site.register(ServiceType)
admin.site.register(RequestStatus)
