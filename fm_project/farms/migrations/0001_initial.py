# Generated by Django 3.1.7 on 2021-04-14 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_number', models.CharField(max_length=250)),
                ('street_name', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('address_type', models.CharField(choices=[('work', 'work'), ('home', 'home'), ('postal', 'postal'), ('contact', 'contact'), ('billing', 'billing')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=250)),
                ('bank_code', models.CharField(max_length=250)),
                ('account_type', models.CharField(choices=[('saving', 'saving'), ('current', 'current'), ('fixed_deposit', 'fixed_deposit')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=250)),
                ('country_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('other_names', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=7, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('date_record_updated', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.address')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.country')),
            ],
        ),
        migrations.CreateModel(
            name='LocalGovernmentArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_government_code', models.CharField(max_length=250)),
                ('local_government_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.IntegerField()),
                ('item_delivery_date', models.DateField()),
                ('vat', models.DecimalField(decimal_places=2, max_digits=11)),
                ('item_status', models.CharField(choices=[('cancelled', 'cancelled'), ('return', 'return'), ('damaged', 'damaged'), ('on_transit', 'on_transit'), ('shipped', 'shipped'), ('preparing_for_shipment', 'preparing_for_shipment')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_code', models.CharField(max_length=250)),
                ('state_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('transaction_comment', models.CharField(max_length=250)),
                ('other_transaction_details', models.CharField(max_length=250)),
                ('transaction_type', models.CharField(choices=[('payment', 'payment'), ('refund', 'refund')], max_length=50, null=True)),
                ('payment_method', models.CharField(choices=[('bank_transfer', 'bank_transfer'), ('cheque', 'cheque')], max_length=50, null=True)),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.bank')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierAccountOpening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_account_created', models.DateField(auto_now_add=True)),
                ('other_account_details', models.CharField(max_length=250)),
                ('account_number', models.CharField(max_length=250, unique=True)),
                ('account_name', models.CharField(max_length=250, null=True)),
                ('date_account_updated', models.DateField(auto_now=True)),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.bank')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rc_number', models.CharField(max_length=250, unique=True)),
                ('company_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250, unique=True)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=7, null=True)),
                ('supplier_type', models.CharField(choices=[('service_provider', 'service_provider'), ('product_supplier', 'product_supplier')], max_length=50, null=True)),
                ('nature_of_business', models.CharField(max_length=250)),
                ('tax_identification_number', models.CharField(max_length=250, unique=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('date_record_updated', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.address')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.country')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_mode', models.CharField(choices=[('courier', 'courier'), ('truck', 'truck')], max_length=50, null=True)),
                ('item_status', models.CharField(choices=[('cancelled', 'cancelled'), ('return', 'return'), ('damaged', 'damaged'), ('on_transit', 'on_transit'), ('shipped', 'shipped'), ('preparing_for_shipment', 'preparing_for_shipment')], max_length=50, null=True)),
                ('shipping_chargers', models.DecimalField(decimal_places=2, max_digits=11)),
                ('address_type', models.CharField(choices=[('work', 'work'), ('home', 'home'), ('postal', 'postal'), ('contact', 'contact'), ('billing', 'billing')], max_length=50, null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.address')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_description', models.CharField(max_length=250)),
                ('product_category', models.CharField(choices=[('horticulture', 'horticulture'), ('poultry', 'poultry'), ('livestock', 'livestock'), ('fruit_crops', 'fruit_crops'), ('cash_crops', 'cash_crops'), ('cereal_crop', 'cereal_crop'), ('vegetables', 'vegetables'), ('tubers', 'tubers'), ('tools_and_equipments', 'tools_and_equipments'), ('others', 'others')], max_length=50, null=True)),
                ('size', models.CharField(choices=[('extra_small', 'extra_small'), ('small', 'small'), ('medium', 'medium'), ('large', 'large'), ('extra_large', 'extra_large')], max_length=50, null=True)),
                ('unit_of_measurement', models.CharField(choices=[('kg', 'kg'), ('ltr', 'ltr'), ('bag', 'bag'), ('piece', 'piece'), ('feet', 'feet'), ('pack', 'pack')], max_length=50, null=True)),
                ('color', models.CharField(max_length=250)),
                ('weight', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='farms.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vat', models.DecimalField(decimal_places=2, max_digits=11)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=11)),
                ('invoice_date', models.DateField()),
                ('other_invoice_details', models.CharField(max_length=250)),
                ('order_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.orderitem')),
            ],
        ),
        migrations.CreateModel(
            name='DispatchNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatch_date', models.DateField()),
                ('quantity_delivered', models.IntegerField()),
                ('delivered_goods', models.CharField(max_length=250, null=True)),
                ('order_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.orderitem')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('expected_delivery_date', models.DateField()),
                ('size', models.CharField(choices=[('extra_small', 'extra_small'), ('small', 'small'), ('medium', 'medium'), ('large', 'large'), ('extra_large', 'extra_large')], max_length=50, null=True)),
                ('address_type', models.CharField(choices=[('work', 'work'), ('home', 'home'), ('postal', 'postal'), ('contact', 'contact'), ('billing', 'billing')], max_length=50, null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.address')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.customer')),
                ('order_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.orderitem')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='lga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.localgovernmentarea'),
        ),
        migrations.AddField(
            model_name='country',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.state'),
        ),
    ]
