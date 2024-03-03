from django.contrib import admin
from reception.models import Booking, Guest, GuestRoom

# Register your models here.

admin.site.register(Booking)
admin.site.register(Guest)
admin.site.register(GuestRoom)