from django.contrib import admin

# Register your models here.
from .models import Customer, Supplier, Product, Bank, Address, Country, State, LocalGovernmentArea, \
    SupplierAccountOpening, Invoice, DispatchNote, SupplierPayment, OrderItem, CustomerOrder, Shipment


admin.site.register(Supplier)

admin.site.register(Customer)

admin.site.register(Bank)

admin.site.register(Product)

admin.site.register(OrderItem)

admin.site.register(SupplierPayment)

admin.site.register(SupplierAccountOpening)

admin.site.register(State)

admin.site.register(DispatchNote)

admin.site.register(CustomerOrder)

admin.site.register(Invoice)

admin.site.register(Shipment)

admin.site.register(Country)

admin.site.register(Address)

admin.site.register(LocalGovernmentArea)






