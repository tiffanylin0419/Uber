# Generated by Django 4.1.5 on 2023-02-02 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0005_ride_num_passenger_alter_ride_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='num_passenger',
            new_name='number_of_passengers',
        ),
    ]
