# Generated by Django 5.1.1 on 2024-10-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_status_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_facebook', models.CharField(max_length=200)),
                ('social_instagram', models.CharField(max_length=200)),
                ('social_twitter', models.CharField(max_length=200)),
            ],
        ),
    ]
