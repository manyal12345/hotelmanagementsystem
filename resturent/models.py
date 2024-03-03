from django.db import models

class Customer(models.Model):
    """
    Represents a customer of the restaurant.
    """
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    preferences = models.TextField(blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)
    loyalty_points = models.PositiveIntegerField(default=0)
    date_of_birth = models.DateField(null=True, blank=True)
    membership_expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    """
    Represents a reservation made by a customer.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    party_size = models.PositiveIntegerField()
    table = models.ForeignKey('Table', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=100, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    special_occasions = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.name} - {self.reservation_time}"

class Table(models.Model):
    """
    Represents a table in the restaurant.
    """
    STATUS_CHOICES = [('available', 'Available'), ('occupied', 'Occupied'), ('reserved', 'Reserved')]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def choose(self, new_status):
        if new_status in [choice[0] for choice in self.STATUS_CHOICES]:
            self.status = new_status
            self.save()
        else:
            raise ValueError("Invalid status")

    def __str__(self):
        return self.name

class ReservationCalendar(models.Model):
    """
    Represents a calendar of reservations for a day.
    """
    date = models.DateField()
    reservations = models.ManyToManyField(Reservation)
    is_holiday = models.BooleanField(default=False)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return f"Reservation Calendar for {self.date}"

class Notification(models.Model):
    """
    Represents a notification sent to a customer.
    """
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    message = models.TextField()


class Menu(models.Model):
    name = models.CharField(max_length=100)

class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='submenus')
    name = models.CharField(max_length=100)

class FoodItem(models.Model):
    submenu = models.ForeignKey(SubMenu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Order(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)