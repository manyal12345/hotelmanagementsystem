
from rest_framework import serializers
from .models import Guest, Booking, GuestRoom
from management.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = '__all__'

class GuestRoomSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()
    room = RoomSerializer()

    class Meta:
        model = GuestRoom
        fields = '__all__'
