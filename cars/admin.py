from django.contrib import admin
from .models import Car, Brand

@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand', 'factory_year', 'value')


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)