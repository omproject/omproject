# Generated by Django 3.2.8 on 2022-03-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_bookinguser_pay_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinguser',
            name='cancel_payment',
            field=models.BooleanField(default=False),
        ),
    ]