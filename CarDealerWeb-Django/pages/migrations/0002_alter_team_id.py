# Generated by Django 4.2.6 on 2024-01-11 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
