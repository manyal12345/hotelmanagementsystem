# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerViewSet,
    ReservationViewSet,
    TableViewSet,
    ReservationCalendarViewSet,
    NotificationViewSet,
    MenuViewSet,
    SubMenuViewSet,
    FoodItemViewSet,
    OrderViewSet
     )

# Create a router and register viewsets with it
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'tables', TableViewSet)
router.register(r'reservation-calendars', ReservationCalendarViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'submenus', SubMenuViewSet)
router.register(r'food-items', FoodItemViewSet)
router.register(r'orders', OrderViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
