from rest_framework import viewsets, status
from rest_framework.response import Response
from categories.models import Categories
from rest_framework import permissions
from .serializer import SerializeCategories
from utils.permissions import IsOwnerOrReadOnly
from django.shortcuts import redirect, render


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = SerializeCategories
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
    


