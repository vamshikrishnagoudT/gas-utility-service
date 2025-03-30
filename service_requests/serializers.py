from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, ServiceRequest, ServiceType, RequestStatus


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "role")


# User Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ("username", "email", "password", "role")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=validated_data["role"],
        )
        return user


# Service Type Serializer
class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"


# Request Status Serializer
class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestStatus
        fields = "__all__"


# Service Request Serializer
class ServiceRequestSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to correctly map foreign keys
    service_type = serializers.PrimaryKeyRelatedField(queryset=ServiceType.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=RequestStatus.objects.all())
    customer = UserSerializer(read_only=True)  # Show customer details in GET response

    class Meta:
        model = ServiceRequest
        fields = "__all__"

    def create(self, validated_data):
        # Assign customer automatically while creating a request
        request = self.context["request"]
        validated_data["customer"] = request.user
        return super().create(validated_data)
