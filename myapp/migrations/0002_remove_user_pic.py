# Generated by Django 3.2.8 on 2021-11-24 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pic',
        ),
    ]