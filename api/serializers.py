from mofisafe_app.models import Budget, User, Income, Expense
from rest_framework import serializers


class SerializeIncome(serializers.ModelSerializer):
    """This serializers the Income class"""

    class Meta:
        model = Income
        fields = ['id', 'user_id', 'amount', 'source', 'date', 'description', 'category']


class SerializeExpense(serializers.ModelSerializer):
    """ This serializes the expenses"""

    class Meta:
        model = Expense
        fields = ['id', 'user_id', 'amount', 'source', 'date', 'description', 'category', 'payment_method']


class SerializeBudget(serializers.ModelSerializer):
    """ This serializes the expenses"""

    class Meta:
        model = Budget
        fields = ['id','user_id', 'amount', 'source', 'date', 'description', 'category', 'payment_method']