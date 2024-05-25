from rest_framework import serializers
from categories.models import Categories

class SerializeCategories(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'description']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required.")
        return value
