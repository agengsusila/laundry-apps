# Generated by Django 3.0.5 on 2021-04-27 05:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210427_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='certifier_user_id',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]
