# Generated by Django 4.1.4 on 2023-02-09 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0009_order_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]
