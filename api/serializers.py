from e_com.models import *
from rest_framework import serializers

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id','name', 'thumbnail', 'cost_range', 'minimum_deposite','max_days')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'user_number')