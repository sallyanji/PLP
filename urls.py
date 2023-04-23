from django.urls import path
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

from django.urls import path
from .views import country_list

urlpatterns = [
    path('countries/', country_list, name='country_list'),
]

from django.urls import path
from .views import bus_list

urlpatterns = [
    path('buses/', bus_list, name='bus_list'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transit_tix.urls')),
]
