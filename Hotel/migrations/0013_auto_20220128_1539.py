# Generated by Django 3.2.8 on 2022-01-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0012_auto_20220128_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='swmming_phool',
        ),
        migrations.AddField(
            model_name='hotel',
            name='swimming_pooll',
            field=models.FileField(blank=True, null=True, upload_to='swimming pool'),
        ),
    ]
