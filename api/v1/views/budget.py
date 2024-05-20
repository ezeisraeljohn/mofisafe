from rest_framework import permissions
from rest_framework import viewsets
from api.v1.serializers import SerializeBudget
from api.v1.permissions import IsOwnerOrReadOnly
from budget.models import Budget


class BudgetViewSet(viewsets.ModelViewSet):
        
    queryset = Budget.objects.all()
    serializer_class = SerializeBudget
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]