from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
from .models import ServiceRequest, ServiceType, RequestStatus

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user




# Service Type Serializer
class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'

# Request Status Serializer
class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestStatus
        fields = '__all__'

# Service Request Serializer
class ServiceRequestSerializer(serializers.ModelSerializer):
    service_type = ServiceTypeSerializer(read_only=True)
    status = RequestStatusSerializer(read_only=True)

    class Meta:
        model = ServiceRequest
        fields = '__all__'
