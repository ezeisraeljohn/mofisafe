from .models import Categories
from rest_framework import serializers


class SerializeCategories(serializers.ModelSerializer):
    """ This serializes the categories"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Categories
        fields = ['id', 'name', 'description']