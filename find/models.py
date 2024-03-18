from django.db import models

# Create your models here.
from django.db import models

class FoodTruck(models.Model):
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    food_items = models.TextField()
    location_description = models.TextField()

