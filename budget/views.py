from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from .serializer import SerializeBudget
from utils.permissions import IsOwnerOrReadOnly
from .models import Budget


class BudgetViewSet(viewsets.ModelViewSet):
        
    queryset = Budget.objects.all()
    serializer_class = SerializeBudget
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)