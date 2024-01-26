from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Fleet
from .models import AircraftQuantity


# Create your views here.
def fleets(request):
    fleet_list = Fleet.objects.all()
    fleet_count = Fleet.objects.count()
    fleet_aircrafts = AircraftQuantity.objects.filter().all()
    context={
        'fleet_list': fleet_list,
        'fleet_count': fleet_count,
        'fleet_aircrafts': fleet_aircrafts
    }
    return render(request, 'fleet/fleet.html', context)
