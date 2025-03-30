from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceRequestViewSet,
    ServiceTypeViewSet,
    RequestStatusViewSet,
    RegisterView,
    UserProfileView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create Router
router = DefaultRouter()

# Register Endpoints with Router
router.register("service-requests", ServiceRequestViewSet, basename="service-requests")
router.register("service-types", ServiceTypeViewSet, basename="service-types")
router.register("request-statuses", RequestStatusViewSet, basename="request-statuses")

# Define URL Patterns
urlpatterns = [
    # User Authentication and Profile
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    # Include router URLs
    path("", include(router.urls)),
]
