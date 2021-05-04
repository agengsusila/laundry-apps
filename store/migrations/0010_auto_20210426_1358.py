# Generated by Django 3.0.5 on 2021-04-26 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.OrderItem'),
        ),
        migrations.DeleteModel(
            name='StaffTable',
        ),
    ]
