from django.db import models
from django.contrib.auth.models import User
from management.models import Room

class Guest(models.Model):
    """
    Represents a guest of the hotel.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    """
    Represents a booking made by a guest.
    """
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    checkin_time = models.TimeField()
    checkout_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.guest} - {self.room} - {self.checkin_date}"

class GuestRoom(models.Model):
    """
    Represents a guest's stay in a room.
    """
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE, related_name='guest_rooms')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkin_time = models.TimeField()
    checkout_date = models.DateField()
    checkout_time = models.TimeField(blank=True, null=True)

    class Meta:
        ordering = ('-checkin_date', '-checkin_time')

    def __str__(self):
        return f"{self.guest} - {self.room} - {self.checkin_date}"