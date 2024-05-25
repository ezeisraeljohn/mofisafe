from rest_framework import viewsets, status
from rest_framework.response import Response
from categories.models import Categories
from rest_framework import permissions
from .serializer import SerializeCategories
from utils.permissions import IsOwnerOrReadOnly
from .forms import CategoryForm
from django.shortcuts import redirect, render


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = SerializeCategories
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
