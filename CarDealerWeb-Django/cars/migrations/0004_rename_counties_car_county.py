# Generated by Django 4.2.6 on 2024-01-11 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_state_car_counties'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='counties',
            new_name='county',
        ),
    ]
