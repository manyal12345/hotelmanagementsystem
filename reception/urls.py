# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuestViewSet, BookingViewSet, GuestRoomViewSet

router = DefaultRouter()
router.register(r'guests', GuestViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'guest-rooms', GuestRoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
