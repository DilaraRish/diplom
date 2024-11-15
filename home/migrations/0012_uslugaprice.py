# Generated by Django 5.1.1 on 2024-10-11 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_usluga'),
    ]

    operations = [
        migrations.CreateModel(
            name='UslugaPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.usluga')),
            ],
        ),
    ]
