# Generated by Django 3.2.8 on 2022-01-28 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0014_auto_20220128_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='swimming_pooll',
            new_name='swimming_pool',
        ),
    ]
