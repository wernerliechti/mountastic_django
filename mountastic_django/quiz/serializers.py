from rest_framework import serializers
from .models import Mountain

class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = ['name', 'image', 'height', 'region', 'group']