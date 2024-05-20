from rest_framework import viewsets
from expenses.models import Expense
from rest_framework import permissions
from api.v1.serializers import SerializeExpense
from api.v1.permissions import IsOwnerOrReadOnly




class ExpenseViewSet(viewsets.ModelViewSet):
    
    queryset = Expense.objects.all()
    serializer_class = SerializeExpense
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]