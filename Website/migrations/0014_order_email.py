# Generated by Django 4.1.4 on 2023-02-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0013_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Email',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
