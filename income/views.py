from rest_framework import generics, permissions, viewsets, status
from .models import Income
from .serializer import SerializeIncome
from rest_framework.response import Response
from utils.permissions import IsOwnerOrReadOnly
from django.utils import timezone


class IncomeViewSet(viewsets.ModelViewSet):

    queryset = Income.objects.all()
    serializer_class = SerializeIncome
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        if 'date' not in serializer.validated_data:
            serializer.save(user=self.request.user, date=timezone.now())
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
