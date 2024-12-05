from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login_view"),
    path('logout_view', views.logout_view, name="logout_view")
]
