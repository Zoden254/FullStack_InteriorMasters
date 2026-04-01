from e_com.models import *
from rest_framework import serializers

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id','name', 'thumbnail', 'cost_range', 'minimum_deposite','max_days')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','profile_pic', 'password', 'user_number')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)