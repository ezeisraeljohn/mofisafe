from mofisafe_app.models import Budget, User, Income, Expense
from rest_framework import serializers


class SerializeIncome(serializers.ModelSerializer):
    """This serializers the Income class"""

    class Meta:
        model = Income
        fields = ['id', 'owner', 'amount', 'source', 'date', 'description', 'category']


class SerializeExpense(serializers.ModelSerializer):
    """ This serializes the expenses"""

    class Meta:
        model = Expense
        fields = ['id', 'owner', 'amount', 'source', 'date', 'description', 'category', 'payment_method']


class SerializeBudget(serializers.ModelSerializer):
    """ This serializes the expenses"""

    class Meta:
        model = Budget
        fields = ['id','owner', 'amount', 'source', 'date', 'description', 'category', 'payment_method']

class SerializeUser(serializers.ModelSerializer):
    """Serializes users"""

    income = SerializeIncome(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'income']