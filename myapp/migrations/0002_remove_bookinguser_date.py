# Generated by Django 3.2.8 on 2022-02-05 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinguser',
            name='date',
        ),
    ]