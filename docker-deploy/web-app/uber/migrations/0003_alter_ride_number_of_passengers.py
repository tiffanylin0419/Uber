# Generated by Django 4.1.5 on 2023-02-05 04:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0002_ride_sharer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='number_of_passengers',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)]),
        ),
    ]
