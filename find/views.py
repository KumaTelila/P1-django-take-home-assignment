from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import FoodTruck
from geopy.distance import geodesic

def find_food_trucks_nearby(latitude, longitude, num_trucks=5):
    trucks = FoodTruck.objects.all()
    distances = [(truck, geodesic((latitude, longitude), (truck.latitude, truck.longitude)).miles) for truck in trucks]
    sorted_trucks = sorted(distances, key=lambda x: x[1])[:num_trucks]
    return sorted_trucks

def index(request):
    if request.method == 'POST':
        latitude = float(request.POST['latitude'])
        longitude = float(request.POST['longitude'])
        nearby_trucks = find_food_trucks_nearby(latitude, longitude)
        return render(request, 'result.html', {'nearby_trucks': nearby_trucks})
    return render(request, 'index.html')

