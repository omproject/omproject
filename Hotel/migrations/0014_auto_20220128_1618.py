# Generated by Django 3.2.8 on 2022-01-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0013_auto_20220128_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='bed_room',
            field=models.FileField(blank=True, null=True, upload_to='bed_room'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='beds_room',
            field=models.FileField(blank=True, null=True, upload_to='beds_room'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_frontview',
            field=models.FileField(blank=True, null=True, upload_to='hotel_frontview'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='swimming_pooll',
            field=models.FileField(blank=True, null=True, upload_to='swimming_pool'),
        ),
    ]
