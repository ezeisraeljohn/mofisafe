from .models import Budget
from rest_framework import serializers


class SerializeBudget(serializers.HyperlinkedModelSerializer):
    """ This serializes the expenses"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Budget
        fields = ['url', 'id', 'user', 'amount']