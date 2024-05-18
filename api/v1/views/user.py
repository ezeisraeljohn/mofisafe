from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from api.v1.serializers import SerializeUser
from django.contrib.auth.models import User


@permission_classes([AllowAny])
class UserList(generics.ListAPIView):
    """ This gets all users """
    queryset = User.objects.all()
    serializer_class = SerializeUser

@permission_classes([AllowAny])
class UserDetail(generics.RetrieveAPIView):
    """ This retrieves a user """
    queryset = User.objects.all()
    serializer_class = SerializeUser

