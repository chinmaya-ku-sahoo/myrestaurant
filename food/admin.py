from django.contrib import admin

# Register your models here.
from .apps import FoodConfig
admin.register(FoodConfig)
