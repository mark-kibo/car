# Generated by Django 4.2.6 on 2024-01-11 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_car_fuel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_style',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Station Wagon', 'Station Wagon'), ('Coupe', 'Coupe'), ('Sports car', 'Sports car'), ('Hatchback', 'Hatchback'), ('Van', 'Van'), ('Pickup', 'Pickup')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=100),
        ),
    ]
