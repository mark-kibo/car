# Generated by Django 4.2.6 on 2024-01-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Manual Transmission', 'Manual Transmission'), ('Automatic Transmission', 'Automatic Transmission')], max_length=100),
        ),
    ]
