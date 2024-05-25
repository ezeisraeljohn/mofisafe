from .models import Expense
from rest_framework import serializers
from django.utils import timezone


class SerializeExpense(serializers.ModelSerializer):
    """ This serializes the expenses"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Expense
        fields = ['user', 'amount', 'source', 'date', 'description', 'category', 'payment_method']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive number.")
        return value
    
    def validate_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Date cannot be in the future")
        return value
    
    def validate_payment_method(self, value):
        allowed_payment_methods = ['Cash', 'Credit Card', 'Debit Card', 'Bank Transfer']
        if value not in allowed_payment_methods:
            raise serializers.ValidationError(f"Payment method must be one of {allowed_payment_methods}")
        return value
    
    def validate_source(self, value):
        if not value.get('source'):
            raise serializers.ValidationError("Source field cannot be empty.")
        return value