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


    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Income.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        if 'date' not in serializer.validated_data:
            serializer.save(user=self.request.user, date=timezone.now())

        amount = serializer.validated_data.get('amount')
        category = serializer.validated_data.get('category')
        user = self.request.user
        
        if category.user != user:
            return Response({"Error":"This category does not belong to you"})

        category.category_balance += amount

        category.save()

        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
