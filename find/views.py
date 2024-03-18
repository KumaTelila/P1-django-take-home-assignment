from django.http import JsonResponse
from django.shortcuts import render
from .models import FoodTruck
from geopy.distance import geodesic
import folium

def find_food_trucks_nearby(latitude, longitude, num_trucks=5):
    # Initialize map centered at the selected location
    map_center = [latitude, longitude]
    mp = folium.Map(location=map_center, zoom_start=12)

    # Get nearby food trucks
    trucks = FoodTruck.objects.all()
    distances = [(truck, geodesic((latitude, longitude), (truck.latitude, truck.longitude)).miles) for truck in trucks]
    sorted_trucks = sorted(distances, key=lambda x: x[1])[:num_trucks]

    # Add markers for nearby food trucks
    for truck, distance in sorted_trucks:
        # Use red color for the first five nearest trucks
        color = 'red'
        folium.Marker(location=[truck.latitude, truck.longitude], popup=(truck.facility_type, truck.address), icon=folium.Icon(color=color)).add_to(mp)

    # Add truck names to a list
    truck_names = [truck for truck, distance in sorted_trucks]

    # Save map to HTML and return HTML content and truck names
    map_html = mp._repr_html_()
    return map_html, truck_names

def index(request):
    return render(request, 'index.html')

def find_food_trucks(request):
    if request.method == 'GET':
        if 'latitude' in request.GET and 'longitude' in request.GET:
            latitude = float(request.GET['latitude'])
            longitude = float(request.GET['longitude'])
            nearby_trucks_map, nearby_trucks = find_food_trucks_nearby(latitude, longitude)
            return render(request, 'result.html', {'nearby_trucks_map': nearby_trucks_map, 'nearby_trucks': nearby_trucks})
        else:
            return render(request, 'result.html', {'error': 'Latitude and longitude parameters are required.'})
    else:
        return render(request, 'result.html', {'error': 'Only GET requests are allowed.'})
