from rest_framework import serializers
from .models import Category


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_color')
        read_only_fields = ('id', 'user')

