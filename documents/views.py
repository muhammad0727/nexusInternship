from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Document
from .serializers import DocumentSerializer


# Create your views here.
class DocumentViewSet(viewsets.ModelViewSet):
    # queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, upload_to='files/')
