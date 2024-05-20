from django.contrib.auth.models import User
from rest_framework import serializers



class SerializeUser(serializers.HyperlinkedModelSerializer):
    """Serializes users"""
    income = serializers.HyperlinkedRelatedField(many=True, view_name='income-detail', read_only=True)
    expenses = serializers.HyperlinkedRelatedField(many=True, view_name='expense-detail', read_only=True)
    budgets = serializers.HyperlinkedRelatedField(many=True, view_name='budget-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url','id', 'username', 'income', 'expenses', 'budgets']