# Generated by Django 5.1.3 on 2024-11-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order_payment_id_order_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=1000),
        ),
    ]
