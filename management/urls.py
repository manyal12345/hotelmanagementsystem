from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomTypeViewSet, RoomViewSet, EmployeeInfoViewSet

router = DefaultRouter()
router.register(r'room-types', RoomTypeViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'employees', EmployeeInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
