from django.urls import path
from . import views

app_name = "car"

urlpatterns = [
    path('', views.CarsListView.as_view(), name="cars_list"),
    path('new_car/', views.NewCarCreateView.as_view(), name="new_car")
]
