from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from .models import Meeting
from .serializers import MeetingSerializer
from django.db.models import Q

# Create your views here.
class MeetingViewSet(viewsets.ModelViewSet):
    # queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Meeting.objects.filter(participants=user) | Meeting.objects.filter(organizer=user)

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    
