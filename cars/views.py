from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Car
from .forms import CarModelForm


    
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

           
        
    
class NewCarCreateView(LoginRequiredMixin, CreateView):
    login_url = 'accounts:login_view'

    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = reverse_lazy('car:new_car')

    def form_valid(self, form):
        messages.success(self.request, "Create success car")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "mistake in creating a car")
        return super().form_invalid(form)
    

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    
    