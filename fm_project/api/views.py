from django.shortcuts import render
from rest_framework import generics, permissions
from farms.models import Product, Supplier, Customer, SupplierAccountOpening, Invoice, DispatchNote, CustomerOrder, \
    Shipment
from .serializers import ProductSerializer, SupplierSerializer, CustomerSerializer, SupplierAccountOpeningSerializer, \
    InvoiceSerializer, DispatchNoteSerializer, CustomerOrderSerializer, ShipmentSerializer


# Create your views here.


class ProductAPIView(generics.ListAPIView):  # this class is used for a get request, it returns a list.
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIPost(generics.ListCreateAPIView):  # This class is used for a post request
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductPatch(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierAPIView(generics.ListAPIView):  # this class is used for a get request, it returns a list.
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierAPIPost(generics.ListCreateAPIView):  # This class is used for a post request
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierPatch(generics.RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDestroy(generics.RetrieveDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CustomerAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SupplierAccountOpeningAPIView(generics.ListAPIView):
    queryset = SupplierAccountOpening.objects.all()
    serializer_class = SupplierAccountOpeningSerializer


class InvoiceAPIView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class DispatchNoteAPIView(generics.ListAPIView):
    queryset = DispatchNote.objects.all()
    serializer_class = DispatchNoteSerializer


class CustomerOrderAPIView(generics.ListAPIView):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer


class ShipmentAPIView(generics.ListAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


