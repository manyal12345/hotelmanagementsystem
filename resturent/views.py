from rest_framework import viewsets
from .models import Customer, Reservation, Table, ReservationCalendar, Notification, Menu, SubMenu, FoodItem, Order
from .serializers import CustomerSerializer, ReservationSerializer, TableSerializer, ReservationCalendarSerializer, NotificationSerializer,MenuSerializer, SubMenuSerializer, FoodItemSerializer, OrderSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class ReservationCalendarViewSet(viewsets.ModelViewSet):
    queryset = ReservationCalendar.objects.all()
    serializer_class = ReservationCalendarSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SubMenuViewSet(viewsets.ModelViewSet):
    queryset = SubMenu.objects.all()
    serializer_class = SubMenuSerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer