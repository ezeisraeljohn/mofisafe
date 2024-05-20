from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from income.models import Income
from income.serializer import SerializeIncome
from api.v1.permissions import IsOwnerOrReadOnly


class IncomeViewSet(viewsets.ModelViewSet):

    queryset = Income.objects.all()
    serializer_class = SerializeIncome
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]