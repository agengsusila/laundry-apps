# Generated by Django 3.0.5 on 2021-04-26 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210426_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='order_item',
        ),
    ]
