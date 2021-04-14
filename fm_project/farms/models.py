from django.db import models

# Create your models here.


class Gender(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'


class AddressType(models.TextChoices):
    WORK = 'work'
    HOME = 'home'
    POSTAL = 'postal'
    CONTACT = 'contact'
    BILLING = 'billing'


class UnitOfMeasurement(models.TextChoices):
    KG = 'kg'
    LTR = 'ltr'
    BAG = 'bag'
    PIECE = 'piece'
    FEET = 'feet'
    PACK = 'pack'


class PaymentMethod(models.TextChoices):
    BANK_TRANSFER = 'bank_transfer'
    CHEQUE = 'cheque'


class AccountType(models.TextChoices):
    SAVING = 'saving'
    CURRENT = 'current'
    FIXED = 'fixed_deposit'


class SupplierType(models.TextChoices):
    SERVICE_PROVIDER = 'service_provider'
    PRODUCT_SUPPLIER = 'product_supplier'


class Facility(models.TextChoices):
    OWN = 'own'
    LEASE = 'lease'


class TransactionType(models.TextChoices):
    PAYMENT = 'payment'
    REFUND = 'refund'


class Size(models.TextChoices):
    EXTRA_SMALL = 'extra_small'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    EXTRA_LARGE = 'extra_large'


class ProductCategory(models.TextChoices):
    HORTICULTURE = 'horticulture'
    POULTRY = 'poultry'
    LIVESTOCK = 'livestock'
    FRUIT_CROPS = 'fruit_crops'
    CASH_CROPS = 'cash_crops'
    CEREAL_CROP = 'cereal_crop'
    VEGETABLES = 'vegetables'
    TUBERS = 'tubers'
    TOOLS_AND_EQUIPMENT = 'tools_and_equipments'
    OTHERS = 'others'


class ItemStatus(models.TextChoices):
    CANCELLED = 'cancelled'
    RETURN = 'return'
    DAMAGED = 'damaged'
    ON_TRANSIT = 'on_transit'
    SHIPPED = 'shipped'
    PREPARING_FOR_SHIPMENT = 'preparing_for_shipment'


class ShipmentMode(models.TextChoices):
    COURIER = 'courier'
    TRUCK = 'truck'


class Bank(models.Model):
    bank_name = models.CharField(max_length=250)
    bank_code = models.CharField(max_length=250)
    account_type = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in AccountType], null=True)

    def __str__(self):
        return self.bank_name


class Address(models.Model):
    street_number = models.CharField(max_length=250)
    street_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    address_type = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in AddressType], null=True)

    def __str__(self):
        return "%s %s %s" % (self.street_number, self.street_name, self.city)


class Shipment(models.Model):
    shipment_mode = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in ShipmentMode], null=True)
    item_status = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in ItemStatus], null=True)
    shipping_chargers = models.DecimalField(max_digits=11, decimal_places=2)
    address_type = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in AddressType], null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.shipping_chargers


class OrderItem(models.Model):
    order_quantity = models.IntegerField()
    item_delivery_date = models.DateField()
    vat = models.DecimalField(max_digits=11, decimal_places=2)
    item_status = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in ItemStatus], null=True)

    def __str__(self):
        return "%s %s %s" % (self.order_quantity, self.item_delivery_date, self.vat)


class SupplierPayment(models.Model):
    transaction_date = models.DateField()
    transaction_amount = models.DecimalField(max_digits=11, decimal_places=2)
    transaction_comment = models.CharField(max_length=250)
    other_transaction_details = models.CharField(max_length=250)
    transaction_type = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in TransactionType], null=True)
    payment_method = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in PaymentMethod], null=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s %s" % (self.transaction_date, self.transaction_amount, self.transaction_comment)


class DispatchNote(models.Model):
    dispatch_date = models.DateField()
    quantity_delivered = models.IntegerField()
    delivered_goods = models.CharField(max_length=250, null=True)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s" % (self.dispatch_date, self.quantity_delivered)


class Invoice(models.Model):
    vat = models.DecimalField(max_digits=11, decimal_places=2)
    commission = models.DecimalField(max_digits=11, decimal_places=2)
    invoice_date = models.DateField()
    other_invoice_details = models.CharField(max_length=250)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s %s %s" % (self.vat, self.commission, self.invoice_date, self.other_invoice_details)


class SupplierAccountOpening(models.Model):
    date_account_created = models.DateField(auto_now_add=True)
    other_account_details = models.CharField(max_length=250)
    account_number = models.CharField(max_length=250, unique=True)
    account_name = models.CharField(max_length=250, null=True)
    date_account_updated = models.DateField(auto_now=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s" % (self.account_number, self.date_account_updated)


class State(models.Model):
    state_code = models.CharField(max_length=250)
    state_name = models.CharField(max_length=250)

    def __str__(self):
        return self.state_name


class LocalGovernmentArea(models.Model):
    local_government_code = models.CharField(max_length=250)
    local_government_name = models.CharField(max_length=250)

    def __str__(self):
        return self.local_government_name


class Country(models.Model):
    country_code = models.CharField(max_length=250)
    country_name = models.CharField(max_length=250)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    lga = models.ForeignKey(LocalGovernmentArea, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.country_name


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    other_names = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=7, choices=[(tag, tag.value) for tag in Gender], null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_record_updated = models.DateTimeField(auto_now=True)

    # password = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.last_name, self.phone_number, self.date_registered)


class Supplier(models.Model):
    rc_number = models.CharField(max_length=250, unique=True)
    company_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250, unique=True)
    email_address = models.EmailField(unique=True)
    gender = models.CharField(max_length=7, choices=[(tag, tag.value) for tag in Gender], null=True)
    supplier_type = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in SupplierType], null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    nature_of_business = models.CharField(max_length=250)
    tax_identification_number = models.CharField(max_length=250, unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_record_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s" % (self.rc_number, self.company_name, self.phone_number, self.date_record_updated)


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_description = models.CharField(max_length=250)
    product_category = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in ProductCategory], null=True)
    size = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in Size], null=True)
    unit_of_measurement = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in UnitOfMeasurement], null=True)
    color = models.CharField(max_length=250)
    weight = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s %s %s" % (self.product_name, self.product_description, self.price)


class CustomerOrder(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in Size], null=True)
    address_type = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in AddressType], null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.order_date


