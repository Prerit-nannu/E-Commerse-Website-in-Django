# Generated by Django 4.1.4 on 2023-02-14 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0020_remove_order_customer_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
