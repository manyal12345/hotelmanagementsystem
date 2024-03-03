from django.db import models
from user.models import CustomUser

class RoomType(models.Model):
    """
    Represents a type of room in the hotel.
    """
    NAME_CHOICES = [('Deluxe Room', 'Deluxe Room'), ('Standard Room', 'Standard Room'), ('Normal Room', 'Normal Room')]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    room_type = models.CharField(max_length=20, choices=NAME_CHOICES)

    def __str__(self):
        return self.name

class Room(models.Model):
    """
    Represents a room in the hotel.
    """
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE, related_name='rooms')
    room_number = models.IntegerField()

    class Meta:
        ordering = ('room_number',)

    def __str__(self):
        return f"{self.room_type} - {self.room_number}"

class EmployeeInfo(models.Model):
    """
    Represents an employee of the hotel.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    hire_date = models.DateField()
    status = models.CharField(max_length=20)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"