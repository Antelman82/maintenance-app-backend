from rest_framework import serializers
from logs.models import User, Vehicle, Log

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Vehicle Serializer
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

# Log Serializer
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
    
    # this might be where I have to verify where the file needs to go before sending back to the api.py