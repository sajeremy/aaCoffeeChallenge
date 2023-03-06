from rest_framework import serializers
from .models import Coffee, Post


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ('id', 'name', 'year',
                  'caffine_content', 'caffine_percentage')
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'coffee', 'text', 'rating', 'created_at')
