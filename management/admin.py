from django.contrib import admin
from management.models import Room, RoomType, EmployeeInfo

# Register your models here.


admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(EmployeeInfo,
                    list_display=('first_name','last_name', 'position'),
)



