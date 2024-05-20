from budget.models import Budget
from income.models import Income
from expenses.models import Expense
from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import models


class SerializeIncome(serializers.HyperlinkedModelSerializer):
    """This serializers the Income class"""
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Income
        fields = ['url', 'id', 'user', 'amount', 'source', 'date', 'category']


class SerializeExpense(serializers.ModelSerializer):
    """ This serializes the expenses"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Expense
        fields = ['id', 'user', 'amount', 'source', 'date', 'description', 'category', 'payment_method']


class SerializeBudget(serializers.HyperlinkedModelSerializer):
    """ This serializes the expenses"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Budget
        fields = ['url', 'id', 'user', 'amount']

class SerializeUser(serializers.HyperlinkedModelSerializer):
    """Serializes users"""
    income = serializers.HyperlinkedRelatedField(many=True, view_name='income-detail', read_only=True)
    expenses = serializers.HyperlinkedRelatedField(many=True, view_name='expense-detail', read_only=True)
    budgets = serializers.HyperlinkedRelatedField(many=True, view_name='budget-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url','id', 'username', 'income', 'expenses', 'budgets']
