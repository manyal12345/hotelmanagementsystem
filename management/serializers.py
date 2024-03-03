from rest_framework import serializers
from .models import RoomType, Room, EmployeeInfo
from user.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = '__all__'

class EmployeeInfoSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = EmployeeInfo
        fields = '__all__'
