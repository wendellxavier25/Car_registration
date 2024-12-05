from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView
from .models import Car
from .forms import CarModelForm


    
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        seacrh = self.request.GET.get('search')
        
        if seacrh:
            cars = cars.filter(model__icontains=seacrh)
        return cars




class NewCarView(LoginRequiredMixin, View):
    login_url = 'accounts:login_view'

    def get(self, request):
        car_form = CarModelForm()
        return render(request, 'new_car.html', {'car_form': car_form})
    
    def post(self, request):
        car_form = CarModelForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            return redirect('car:cars_list')
        return redirect('car:new_car')