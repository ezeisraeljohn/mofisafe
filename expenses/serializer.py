from .models import Expense
from rest_framework import serializers


class SerializeExpense(serializers.ModelSerializer):
    """ This serializes the expenses"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Expense
        fields = ['id', 'user', 'amount', 'source', 'date', 'description', 'category', 'payment_method']