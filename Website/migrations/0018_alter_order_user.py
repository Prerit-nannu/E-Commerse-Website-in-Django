# Generated by Django 4.1.4 on 2023-02-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0017_remove_order_user_id_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.IntegerField(default='1'),
        ),
    ]