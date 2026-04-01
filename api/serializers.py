from e_com.models import Service
from rest_framework import serializers

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'thumbnail', 'cost_range')