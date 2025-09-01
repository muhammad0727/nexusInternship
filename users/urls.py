from django.urls import path
from .views import UserRegistrationView, UserProfileView, GenerateOTPView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('profile/generate-otp', GenerateOTPView.as_view(), name='generate-otp')
]

