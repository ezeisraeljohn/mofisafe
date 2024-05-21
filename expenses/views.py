from rest_framework import viewsets
from .models import Expense
from rest_framework import permissions
from .serializer import SerializeExpense
from utils.permissions import IsOwnerOrReadOnly




class ExpenseViewSet(viewsets.ModelViewSet):
    
    queryset = Expense.objects.all()
    serializer_class = SerializeExpense
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]