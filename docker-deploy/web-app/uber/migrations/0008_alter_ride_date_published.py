# Generated by Django 4.1.5 on 2023-02-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0007_remove_ride_pub_date_ride_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='date_published',
            field=models.DateTimeField(),
        ),
    ]