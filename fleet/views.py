from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Fleet
from .models import AircraftQuantity
from .forms import FleetSelectorForm

# Create your views here.
def fleets(request):
    #fleet list and form for context
    fleets = Fleet.objects.all()
    form = FleetSelectorForm()
    
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FleetSelectorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            selected = form.cleaned_data['fleet_selector']
            fleet_aircrafts = AircraftQuantity.objects.filter(fleet = selected).all()
            context={
                'fleets': fleets,
                'form': FleetSelectorForm(),
                'selection': selected,
                'fleet_aircrafts': fleet_aircrafts
            }
            return render(request, 'fleet/fleet.html', context)
    else:
        form = FleetSelectorForm()
        
        context={
            'fleets': fleets,
            'form': FleetSelectorForm(),
            'selected': None,
            'fleet_aircrafts': None,
        }
        return render(request, 'fleet/fleet.html', context)