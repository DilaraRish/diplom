# Generated by Django 5.1.1 on 2024-10-13 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_status_remove_stoimost_name_order_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
