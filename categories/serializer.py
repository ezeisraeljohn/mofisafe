from rest_framework import serializers
from categories.models import Categories

class SerializeCategories(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'url', 'name', 'description', 'user']
        read_only_fields = ['user']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required.")
        return value
