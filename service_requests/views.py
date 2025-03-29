from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, ServiceRequest, ServiceType, RequestStatus
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    ServiceRequestSerializer,
    ServiceTypeSerializer,
    RequestStatusSerializer,
)

# ✅ User Registration API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# ✅ Get User Profile
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# ✅ Custom Permission: Role-Based Access Control (RBAC)
class IsCustomerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == "customer"

    def has_object_permission(self, request, view, obj):
        # Admin can access all requests
        if request.user.role == "admin":
            return True
        # Support can update requests
        if request.user.role == "support" and request.method == "PUT":
            return True
        # Customer can only access their own requests
        return obj.customer == request.user


# ✅ Service Request ViewSet
class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated, IsCustomerOrReadOnly]

    def perform_create(self, serializer):
        # Save the request with the authenticated customer
        serializer.save(customer=self.request.user)


# ✅ Service Type ViewSet (Admin Only)
class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAdminUser]


# ✅ Request Status ViewSet (Admin Only)
class RequestStatusViewSet(viewsets.ModelViewSet):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer
    permission_classes = [IsAdminUser]
