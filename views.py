from django.shortcuts import render
from .models import Bus

def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})
