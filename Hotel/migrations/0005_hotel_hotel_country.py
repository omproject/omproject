# Generated by Django 3.2.8 on 2022-01-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0004_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_country',
            field=models.CharField(default='india', max_length=20),
        ),
    ]
