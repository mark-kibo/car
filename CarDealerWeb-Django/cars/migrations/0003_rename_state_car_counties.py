# Generated by Django 4.2.6 on 2024-01-11 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_car_miles_remove_car_vin_no_alter_car_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='state',
            new_name='counties',
        ),
    ]