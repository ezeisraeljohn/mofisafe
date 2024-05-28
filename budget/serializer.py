from .models import Budget
from rest_framework import serializers
from django.utils import timezone
from django.utils.dateparse import parse_datetime


class SerializeBudget(serializers.ModelSerializer):
    """ This serializes the expenses"""

    class Meta:
        model = Budget
        fields = ['id', 'url', 'user', 'amount', 'period', 'start_date', 'end_date']
        read_only_fields = ['user']

    def validate(self, data):
        start_date_str = data.get('start_date')
        end_date_str = data.get('end_date')

        if start_date_str and end_date_str:
            if end_date_str <= start_date_str:
                raise serializers.ValidationError("End date must be after the start date.")
        return data