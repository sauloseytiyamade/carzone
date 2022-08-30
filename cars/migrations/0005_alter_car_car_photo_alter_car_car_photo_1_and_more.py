# Generated by Django 4.1 on 2022-08-29 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_created_date_alter_car_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(upload_to='photos/car/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_1',
            field=models.ImageField(blank=True, upload_to='photos/car/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_2',
            field=models.ImageField(blank=True, upload_to='photos/car/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_3',
            field=models.ImageField(blank=True, upload_to='photos/car/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(blank=True, upload_to='photos/car/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 29, 22, 23, 28, 288951)),
        ),
    ]