# Generated by Django 2.2.2 on 2019-06-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommApp', '0002_customers_orderdetails_orders_payment_products_shippers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='PhoneNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customers',
            name='PinCode',
            field=models.IntegerField(),
        ),
    ]
