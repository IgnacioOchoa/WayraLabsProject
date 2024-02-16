from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Fleet
from .models import AircraftQuantity
from .forms import FleetForm, AcftForm, AcftEditForm

# View to display fleet page -- FUNCTIONAL
def show(request):
    #fleet list and forms for context
    fleets = Fleet.objects.all()
    fleet_form = FleetForm()
    context={
        'fleets': fleets,
        'fleet_form': fleet_form
    }
    return render(request, 'fleet/fleet.html', context)

#View to create fleet -- FUNCTIONAL
def create_fleet(request):  
    if request.method == "POST":  
        form = FleetForm(request.POST)
        if form.is_valid():
            try:  
                form.save()
                return HttpResponseRedirect(reverse('fleets'))  
            except:  
                pass
    else:  
        form = FleetForm()  
    return HttpResponseRedirect(reverse('fleets'))

#View to update fleet name -- FUNCTIONAL
def update_name(request, id): 
    fleet = Fleet.objects.get(id=id)
    if request.method == "POST":
        form = FleetForm(request.POST, instance=fleet)
        if form.is_valid():
            try:  
                form.save()
                return update_fleet(request, id)
            except:  
                pass

#View to update fleet -- FUNCTIONAL
def update_fleet(request, id):  
    fleet = Fleet.objects.get(id=id)
    fleet_aircrafts = AircraftQuantity.objects.filter(fleet = fleet).all()
    fleet_form = FleetForm()
    acft_form = AcftForm()
    acft_edit_form = AcftEditForm()
    context={
        'fleet_aircrafts': fleet_aircrafts,
        'fleet': fleet,
        'fleet_form': fleet_form,
        'acft_form': acft_form,
        'acft_edit_form': acft_edit_form
    }
    return render(request, 'fleet/update.html', context)

# View to delete fleet -- FUNCTIONAL
def destroy_fleet(request, id):  
    fleet = Fleet.objects.get(id=id)  
    fleet.delete()  
    return HttpResponseRedirect(reverse('fleets'))

# View to create acft -- FUNCTIONAL
def create_acft(request, id):
    fleet = Fleet.objects.get(id=id) 
    if request.method == "POST":
        form = AcftForm(request.POST)
        if form.is_valid():
            form.instance.fleet = fleet
            try:  
                form.save()
                return update_fleet(request, id)
            except:
                pass

#View to update fleet aircraft -- NOT FUNCTIONAL ¿HACER FORM ESPECÍFICO?
def update_acft(request, fleet_acft_id):  
    fleet_aircraft = AircraftQuantity.objects.get(id=fleet_acft_id)
    fleet = fleet_aircraft.fleet
    acft = fleet_aircraft.aircraft
    id = fleet.id
    if request.method == "POST":
        form = AcftEditForm(request.POST, instance=fleet_aircraft)
        if form.is_valid():
            form.instance.fleet = fleet
            form.instance.aircraft = acft
            try:  
                form.save()
                return update_fleet(request, id)
            except:
                pass

# View to delete aircraft -- FUNCTIONAL
def destroy_acft(request, fleet_acft_id):
    fleet_aircraft = AircraftQuantity.objects.get(id=fleet_acft_id)   
    fleet = fleet_aircraft.fleet
    id = fleet.id
    fleet_aircraft.delete()
    return update_fleet(request, id)

# View to see acft card -- NOT FUNCTIONAL
def acft_details(request, fleet_acft_id):
    fleet_aircraft = AircraftQuantity.objects.get(id=fleet_acft_id)   
    return render(request, 'fleet/acft_details.html', {'element': fleet_aircraft})

""" RESTA IMPLEMENTAR:
        -- PIECHART FLEET
        -- PIECHART ACFT"""   