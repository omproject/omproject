# Generated by Django 3.2.8 on 2021-12-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0002_user_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
