# views.py
from rest_framework import viewsets
from .models import Guest, Booking, GuestRoom
from .serializers import GuestSerializer, BookingSerializer, GuestRoomSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class GuestRoomViewSet(viewsets.ModelViewSet):
    queryset = GuestRoom.objects.all()
    serializer_class = GuestRoomSerializer
