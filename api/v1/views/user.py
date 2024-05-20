from rest_framework.decorators import permission_classes
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.v1.serializers import SerializeUser
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    """ This gets all users """
    queryset = User.objects.all()
    serializer_class = SerializeUser