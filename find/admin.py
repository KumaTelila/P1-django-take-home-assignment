from django.contrib import admin
from .models import FoodTruck

# Register your models here.
class FoodTruckAdmin(admin.ModelAdmin):
    pass
admin.site.register(FoodTruck, FoodTruckAdmin)