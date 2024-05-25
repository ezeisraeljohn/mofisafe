from rest_framework import viewsets
from categories.models import Categories
from rest_framework import permissions
from .serializer import SerializeCategories
from utils.permissions import IsOwnerOrReadOnly


class CategoriesViewSet(viewsets.ModelViewSet):
    
    queryset = Categories.objects.all()
    serializer_class = SerializeCategories
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]