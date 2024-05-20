from .models import Income
from rest_framework import serializers


class SerializeIncome(serializers.HyperlinkedModelSerializer):
    """This serializers the Income class"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Income
        fields = ['url', 'id', 'user', 'amount', 'source', 'date', 'category']