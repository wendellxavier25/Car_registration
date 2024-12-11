from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('', lambda request: redirect('car:cars_list')),
    path('accounts/', include('accounts.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
