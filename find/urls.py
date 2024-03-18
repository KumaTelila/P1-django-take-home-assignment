from django.urls import path
from . import views
from .views import index, find_food_trucks

urlpatterns = [
    path('', views.index, name='index'),
    path('find_food_trucks/', find_food_trucks, name='find_food_trucks'),
]
