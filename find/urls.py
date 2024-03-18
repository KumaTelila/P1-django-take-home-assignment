from django.urls import path
from . import views
from .views import index, find_food_trucks
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('find_food_trucks/', find_food_trucks, name='find_food_trucks'),
    path('api/food-trucks/', api.FoodTruckListAPIView.as_view(), name='food_truck_list_api'),
]
