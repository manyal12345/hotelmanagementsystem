from django.contrib import admin
from resturent.models import Customer, Reservation, Table, ReservationCalendar, Notification, Menu, SubMenu, FoodItem, Order

# Register your models here.

admin.site.register(
    Customer,
    list_display=['name', 'contact_info', 'date_of_birth', 'membership_expiration_date']
)

admin.site.register(Reservation)
admin.site.register(Table)
admin.site.register(ReservationCalendar)
admin.site.register(Notification)
admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(FoodItem)
admin.site.register(Order)