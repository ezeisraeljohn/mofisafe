from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from .models import Income
from .serializer import SerializeIncome
from utils.permissions import IsOwnerOrReadOnly


class IncomeViewSet(viewsets.ModelViewSet):

    queryset = Income.objects.all()
    serializer_class = SerializeIncome
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]