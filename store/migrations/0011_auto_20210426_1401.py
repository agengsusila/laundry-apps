# Generated by Django 3.0.5 on 2021-04-26 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210426_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='product',
            new_name='order_item',
        ),
    ]
