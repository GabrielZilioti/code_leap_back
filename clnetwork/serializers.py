from rest_framework import serializers
from .models import CLNetwork


class CLNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CLNetwork
        fields = ['id', 'username', 'title', 'content']
