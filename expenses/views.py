from rest_framework import viewsets, status, permissions
from django.utils import timezone
from .models import Expense
from .serializer import SerializeExpense
from rest_framework.response import Response
from utils.permissions import IsOwnerOrReadOnly




class ExpenseViewSet(viewsets.ModelViewSet):
    
    queryset = Expense.objects.all()
    serializer_class = SerializeExpense
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Expense.objects.filter(user=self.request.user)
        return Expense.objects.none()
    
    def perform_create(self, serializer):
        if 'date' not in serializer.validated_data:
            serializer.save(user=self.request.user, date=timezone.now())

        amount = serializer.validated_data.get('amount')
        category = serializer.validated_data.get('category')
        user = self.request.user
        
        if category.user != user:
            return Response({"Error":"This category does not belong to you"})

        category.category_balance -= amount

        category.save()

        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)