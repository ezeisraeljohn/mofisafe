from rest_framework import serializers
from categories.models import Categories

class SerializeCategories(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'type', 'url', 'name', 'description', 'user', 'category_balance']
        read_only_fields = ['user']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required.")
        return value
