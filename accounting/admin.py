from django.contrib import admin
from accounting.models import Invoice, Payment, Transaction, Bill

# Register your models here.

admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Transaction)
admin.site.register(Bill)