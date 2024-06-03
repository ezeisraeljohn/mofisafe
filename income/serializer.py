from .models import Income
from categories.models import Categories
from django.utils import timezone
from rest_framework import serializers


class SerializeIncome(serializers.HyperlinkedModelSerializer):
    """This serializers the Income class"""
    category = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())

    class Meta:
        model = Income
        fields = ['id', 'url', 'user', 'amount', 'source', 'date', 'category']
        read_only_fields = ['user']
        
    def validate_amount(self, value):
        """Ensure the amount is a positive number."""
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive number.")
        return value

    def validate_date(self, value):
        """Ensure the date is not in the future."""
        if value > timezone.now():
            raise serializers.ValidationError("Date cannot be in the future.")
        return value

    def validate_source(self, value):
        """Ensure the source is not empty."""
        if not value:
            raise serializers.ValidationError("Source field cannot be empty.")
        return value

    def validate_category(self, value):
        """Ensure the category is valid."""
        if not Categories.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Category does not exist.")
        return value