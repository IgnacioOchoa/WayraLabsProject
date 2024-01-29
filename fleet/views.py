from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Fleet
from .models import AircraftQuantity
from .forms import FleetSelectorForm

# Create your views here.
def fleets(request):
    fleet_list = Fleet.objects.all()
    fleet_count = Fleet.objects.count()
    # fleet_aircrafts = AircraftQuantity.objects.filter().all()
    form = FleetSelectorForm()
    context={
        'fleet_list': fleet_list,
        'fleet_count': fleet_count,
        # 'fleet_aircrafts': fleet_aircrafts,
        'form': FleetSelectorForm()
    }
    return render(request, 'fleet/fleet.html', context)

def get_fleet(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FleetSelectorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            selected = form.cleaned_data['fleet_selector']
            # load data in page:
            fleet_aircrafts = AircraftQuantity.objects.filter(fleet = selected).all()
            print(fleet_aircrafts)
            context={
                'fleet_aircrafts': fleet_aircrafts,
                'form': FleetSelectorForm()
            }
            return render(request, 'fleet/fleet.html', context)