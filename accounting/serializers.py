from rest_framework import serializers
from .models import Bill, Payment, Invoice, Transaction
from reception.models import Guest
from resturent.models import Order
from reception.serializers import GuestSerializer
from resturent.serializers import OrderSerializer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()

    class Meta:
        model = Bill
        fields = '__all__'
