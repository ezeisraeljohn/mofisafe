from .models import Expense
from income.models import Income
from rest_framework import serializers
from django.utils import timezone


class SerializeExpense(serializers.ModelSerializer):
    """ This serializes the expenses"""

    class Meta:
        model = Expense
        fields = ['id', 'url', 'user', 'amount', 'date', 'description', 'category', 'payment_method']
        read_only_fields = ['user']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive number.")
        return value

    def validate_date(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Date cannot be in the future")
        return value

    def validate_payment_method(self, value):
        allowed_payment_methods = ['Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', ""]
        if value not in allowed_payment_methods:
            raise serializers.ValidationError(f"Payment method must be one of {allowed_payment_methods}")
        return value
    
    def validate_source(self, value):
        if not value.get('source'):
            raise serializers.ValidationError("Source field cannot be empty.")
        return value
