from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('driver', 'make', 'model', 'added_at')
        model = Car