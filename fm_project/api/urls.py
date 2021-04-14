from django.urls import path

from .views import ProductAPIView, ProductAPIPost, SupplierAPIView, SupplierAPIPost, \
    CustomerAPIView, SupplierAccountOpeningAPIView, InvoiceAPIView, DispatchNoteAPIView, CustomerOrderAPIView, \
    ShipmentAPIView, ProductPatch, ProductDestroy, SupplierPatch, SupplierDestroy

urlpatterns = [
    path('get/product', ProductAPIView.as_view()),
    path('post/product', ProductAPIPost.as_view()),
    path('patch/product/<int:pk>', ProductPatch.as_view()),
    path('destroy/product/<int:pk>', ProductDestroy.as_view()),
    path('get/supplier', SupplierAPIView.as_view()),
    path('post/supplier', SupplierAPIPost.as_view()),
    path('patch/supplier/<int:pk>', SupplierPatch.as_view()),
    path('destroy/supplier/<int:pk>', SupplierDestroy.as_view()),
    path('get/customer', CustomerAPIView.as_view()),
    path('get/supplier_account_opening', SupplierAccountOpeningAPIView.as_view()),
    path('get/invoice', InvoiceAPIView.as_view()),
    path('get/dispatch_note', DispatchNoteAPIView.as_view()),
    path('get/customer_order', CustomerOrderAPIView.as_view()),
    path('get/shipment', ShipmentAPIView.as_view()),


]
