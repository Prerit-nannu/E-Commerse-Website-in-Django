# Generated by Django 4.1.4 on 2023-02-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0012_rename_user_id_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
