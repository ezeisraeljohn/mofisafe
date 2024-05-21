from rest_framework import permissions
from rest_framework import viewsets
from .serializer import SerializeBudget
from utils.permissions import IsOwnerOrReadOnly
from .models import Budget


class BudgetViewSet(viewsets.ModelViewSet):
        
    queryset = Budget.objects.all()
    serializer_class = SerializeBudget
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]