# Generated by Django 3.1.7 on 2021-04-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0002_auto_20210416_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
