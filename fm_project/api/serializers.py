from rest_framework import serializers

from farms.models import Product, Supplier, Customer, SupplierAccountOpening, Invoice, DispatchNote, CustomerOrder, Shipment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # used to output all the fields in the model.


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number', 'address']


class SupplierAccountOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierAccountOpening
        fields = ['bank', 'account_number', 'account_name']


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class DispatchNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchNote
        fields = '__all__'


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = '__all__'


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

