from django.core.management.base import BaseCommand
from find.models import FoodTruck
import csv
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = os.path.join('data', 'food-truck-data.csv')
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                FoodTruck.objects.create(
                    applicant=row['Applicant'],
                    facility_type=row['FacilityType'],
                    address=row['Address'],
                    latitude=float(row['Latitude']),
                    longitude=float(row['Longitude']), 
                    food_items = row['FoodItems'],
                    location_description = row['LocationDescription']
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
