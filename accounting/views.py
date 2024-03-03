from rest_framework import viewsets
from .models import Bill, Payment, Invoice, Transaction
from .serializers import BillSerializer, PaymentSerializer, InvoiceSerializer, TransactionSerializer
from rest_framework.filters import SearchFilter

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = [SearchFilter]
    search_fields = ['customer', 'bill_number']

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = [SearchFilter]
    search_fields = ['customer', 'bill_number']

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
