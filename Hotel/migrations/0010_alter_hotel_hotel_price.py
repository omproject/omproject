# Generated by Django 3.2.8 on 2022-01-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0009_alter_hotel_hotel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_price',
            field=models.IntegerField(default=0),
        ),
    ]
