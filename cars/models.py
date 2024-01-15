from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

    id = models.BigAutoField(primary_key=True)
    state_choice = (
        ('NBI', 'Nairobi'),
        ('MSA', 'Mombasa'),
        ('KSM', 'Kisumu'),
        ('KMB', 'Kiambu'),
        ('KWL', 'Kwale'),
        ('KLF', 'Kilifi'),
        ('TRV', 'Tana River'),
        ('LMU', 'Lamu'),
        ('TVT', 'Taita Taveta'),
        ('GRS', 'Garissa'),
        ('WJR', 'Wajir'),
        ('MDR', 'Mandera'),
        ('MRS', 'Marsabit'),
        ('ISL', 'Isiolo'),
        ('MRU', 'Meru'),
        ('TNT', 'Tharaka-Nithi'),
        ('EMB', 'Embu'),
        ('KTU', 'Kitui'),
        ('MCK', 'Machakos'),
        ('MKN', 'Makueni'),
        ('NDR', 'Nyandarua'),
        ('NYR', 'Nyeri'),
        ('KRG', 'Kirinyaga'),
        ('MRG', 'Muranga'),
        ('TRK', 'Turkana'),
        ('WPK', 'West Pokot'),
        ('SBR', 'Samburu'),
        ('TNZ', 'Trans Nzoia'),
        ('UGS', 'Uasin Gishu'),
        ('EMK', 'Elgeyo Marakwet'),
        ('NDI', 'Nandi'),
        ('BRG', 'Baringo'),
        ('LKP', 'Laikipia'),
        ('NKR', 'Nakuru'),
        ('NRK', 'Narok'),
        ('KJD', 'Kajiado'),
        ('KRC', 'Kericho'),
        ('BMT', 'Bomet'),
        ('KKG', 'Kakamega'),
        ('VHG', 'Vihiga'),
        ('BGM', 'Bungoma'),
        ('BSA', 'Busia'),
        ('SYA', 'Siaya'),
        ('HBY', 'Homa Bay'),
        ('MGR', 'Migori'),
        ('KSI', 'Kisii'),
        ('NMR', 'Nyamira'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    model_choices = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Station Wagon','Station Wagon'),
        ('Coupe', 'Coupe'),
        ('Sports car', 'Sports car'),
        ('Hatchback', 'Hatchback'),
        ('Van', 'Van'),
        ('Pickup', 'Pickup'),
    )

    condition_choices = (
        ('Brand New', 'Brand New'),
        ('Foreign Used', 'Foreign Used'),
        ('Kenyan Used', 'Kenyan Used'),
    )
    transmission_choices = (
        ('Manual Transmission', 'Manual Transmission'),
        ('Automatic Transmission', 'Automatic Transmission'),
    )
    fuel_choices = (
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'),
    )
    car_title = models.CharField(max_length=255)
    county = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(choices=condition_choices, max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=100)
    body_style = models.CharField(choices = model_choices, max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(choices=transmission_choices, max_length=100)
    interior = models.CharField(max_length=100)
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    milage = models.IntegerField()
    fuel_type = models.CharField(choices=fuel_choices, max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
