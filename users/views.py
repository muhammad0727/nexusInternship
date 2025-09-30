from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserProfileSerializer

# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny] # Or IsAuthenticated, depending on requirements

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# 2FA implementation
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
import random

class GenerateOTPView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        otp = random.randint(100000,9999999)

        try:
            send_mail(
                "Your Nexus OTP Code",
                f'your otp code is {otp}',
                'noreply@internship.com',
                [user.email],
                fail_silently=False,
            )

            return Response({'message':'OTP sent to your email'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e) + '\n failed to send email, please try again.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            