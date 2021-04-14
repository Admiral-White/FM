from django.test import TestCase


from .models import Product, Supplier, Customer


# Create your tests here.


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(product_name='palm fruits', product_description='improved variety of palm fruit.',
                               product_category='cash_crop', size='small', unit_of_measurement='kg',
                               color='red', weight='50kg', price=5000.00)

    def test_productName(self):
        product = Product.objects.get(pk=1)
        expected_object_name = f'{product.product_name}'
        self.assertEquals(expected_object_name, 'palm fruits')

    def test_product_description(self):
        product = Product.objects.get(pk=1)
        expected_object_name = f'{product.product_description}'
        self.assertEquals(expected_object_name, 'improved variety of palm fruit.')

    def test_product_category(self):
        product = Product.objects.get(pk=1)
        expected_object_name = f'{product.product_category}'
        self.assertEquals(expected_object_name, 'cash_crop')

    def test_size(self):
        product = Product.objects.get(pk=1)
        expected_object_name = f'{product.size}'
        self.assertEquals(expected_object_name, 'small')

    def test_unit_of_measurement(self):
        product = Product.objects.get(pk=1)
        expected_object_name = f'{product.unit_of_measurement}'
        self.assertEquals(expected_object_name, 'kg')

    def test_color(self):
        product = Product.objects.get(pk=1)
        expected_object_name = f'{product.color}'
        self.assertEquals(expected_object_name, 'red')

    def test_weight(self):
        product = Product.objects.get(pk=1)
        expected_object_name = f'{product.weight}'
        self.assertEquals(expected_object_name, '50kg')

    def test_price(self):
        product = Product.objects.get(pk=1)
        expected_object_name = product.price
        self.assertEquals(expected_object_name, 5000.00)


class SupplierTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Supplier.objects.create(rc_number='56732', company_name='debby international farms', phone_number='0809112312',
                                email_address='debby@farms.com', gender='female', supplier_type='product_supplier',
                                nature_of_business='farm business', tax_identification_number='76990')

    def test_rc_number(self):
        supplier = Supplier.objects.get(pk=1)
        expected_object_name = f'{supplier.rc_number}'
        self.assertEquals(expected_object_name, '56732')

    def test_company_name(self):
        supplier = Supplier.objects.get(pk=1)
        expected_object_name = f'{supplier.company_name}'
        self.assertEquals(expected_object_name, 'debby international farms')

    def test_phone_number(self):
        supplier = Supplier.objects.get(pk=1)
        expected_object_name = f'{supplier.phone_number}'
        self.assertEquals(expected_object_name, '0809112312')

    def test_email_address(self):
        supplier = Supplier.objects.get(pk=1)
        expected_object_name = f'{supplier.email_address}'
        self.assertEquals(expected_object_name, 'debby@farms.com')

    def test_gender(self):
        supplier = Supplier.objects.get(pk=1)
        expected_object_name = f'{supplier.gender}'
        self.assertEquals(expected_object_name, 'female')

    def test_supplier_type(self):
        supplier = Supplier.objects.get(pk=1)
        expected_object_name = f'{supplier.supplier_type}'
        self.assertEquals(expected_object_name, 'product_supplier')

    def test_nature_of_business(self):
        supplier = Supplier.objects.get(pk=1)
        expected_object_name = f'{supplier.nature_of_business}'
        self.assertEquals(expected_object_name, 'farm business')

    def test_tax_identification_number(self):
        supplier = Supplier.objects.get(pk=1)
        expected_object_name = f'{supplier.tax_identification_number}'
        self.assertEquals(expected_object_name, '76990')


class CustomerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(first_name='Mike', other_names='Kings', last_name='Max', date_of_birth=(1995-5-25),
                                gender='male', email='mikemax@gmail.com', phone_number='0809125674', password='power123'
                                )

    def test_first_name(self):
        customer = Customer.objects.get(pk=1)
        expected_object_name = f'{customer.first_name}'
        self.assertEquals(expected_object_name, 'Mike')

    def test_other_names(self):
        customer = Customer.objects.get(pk=1)
        expected_object_name = f'{customer.other_names}'
        self.assertEquals(expected_object_name, 'Kings')

    def test_last_name(self):
        customer = Customer.objects.get(pk=1)
        expected_object_name = f'{customer.last_name}'
        self.assertEquals(expected_object_name, 'Max')

    def test_date_of_birth(self):
        customer = Customer.objects.get(pk=1)
        expected_object_name = customer.date_of_birth
        self.assertEquals(expected_object_name, (1991-5-25))

    def test_gender(self):
        customer = Customer.objects.get(pk=1)
        expected_object_name = f'{customer.gender}'
        self.assertEquals(expected_object_name, 'male')

    def test_email(self):
        customer = Customer.objects.get(pk=1)
        expected_object_name = f'{customer.email}'
        self.assertEquals(expected_object_name, 'mikemax@gmail.com')

    def test_phone_number(self):
        customer = Customer.objects.get(pk=1)
        expected_object_name = f'{customer.phone_number}'
        self.assertEquals(expected_object_name, '0809125674')

    def test_password(self):
        customer = Customer.objects.get(pk=1)
        expected_object_name = f'{customer.password}'
        self.assertEquals(expected_object_name, 'power123')


"""note well: before you run any test with a mysql database ensure to grant this privilege on the database script
 >> grant all privileges on test_farm_db_django.* to 'farm'@'localhost' """



