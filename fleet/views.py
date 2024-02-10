from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Fleet
from .models import AircraftQuantity
from .forms import FleetSelectorForm
from .forms import FleetForm

# view to display fleet page -- FUNCTIONAL
def show(request):
    #fleet list and form for context
    fleets = Fleet.objects.all()
    form = FleetForm()
    context={
        'fleets': fleets,
        'form': form
    }
    return render(request, 'fleet/fleet.html', context)

#View to create fleet
def create_fleet(request):  
    if request.method == "POST":  
        print('request is POST')
        form = FleetForm(request.POST)
        if form.is_valid():
            print('form is valid')
            try:  
                form.save()
                print('reloading fleet')
                return HttpResponseRedirect(reverse('fleets'))  
            except:  
                pass
    else:  
        form = FleetForm()  
    return HttpResponseRedirect(reverse('fleets'))  

#View to update fleet
def update_fleet(request, id):  
    fleet = Fleet.objects.get(id=id)
    fleet_aircrafts = AircraftQuantity.objects.filter(fleet = fleet).all()
    context={
        'fleet_aircrafts': fleet_aircrafts,
        'fleet': fleet,
    }
    return render(request, 'fleet/update.html', context)

# View to delete fleet -- FUNCTIONAL
def destroy_fleet(request, id):  
    fleet = Fleet.objects.get(id=id)  
    fleet.delete()  
    return HttpResponseRedirect(reverse('fleets'))

def details_acft(request, fleet_acft_id):
    fleet_aircraft = AircraftQuantity.objects.get(id=fleet_acft_id)   
    return render(request, 'fleet/acft_details.html', {'element': fleet_aircraft})

#View to update fleet aircraft
def update_acft(request, fleet_acft_id):  
    fleet_aircraft = AircraftQuantity.objects.get(id=fleet_acft_id) 
    return render(request, 'fleet/update.html')    

# View to delete aircraft -- FUNCTIONAL
def destroy_acft(request, fleet_acft_id):
    fleet_aircraft = AircraftQuantity.objects.get(id=fleet_acft_id)   
    fleet = fleet_aircraft.fleet
    fleet_aircraft.delete()
    fleet_aircrafts = AircraftQuantity.objects.filter(fleet = fleet).all()
    context={
        'fleet_aircrafts': fleet_aircrafts,
        'fleet': fleet,
    }
    return render(request, 'fleet/update.html', context)





    """ #If request method is "POST"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FleetSelectorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if 'fleet_selector' == '':
                selected = None
            else:
                selected = form.cleaned_data['fleet_selector']

            fleet_aircrafts = AircraftQuantity.objects.filter(fleet = selected).all()
            form.initial = {'fleet_selector': selected.pk}
            context={
                'fleets': fleets,
                'form': form,
                'selection': selected,
                'fleet_aircrafts': fleet_aircrafts
            }
            return render(request, 'fleet/fleet.html', context)
        
        #If form is not valid, default rendering is given
        else:
            context={
                'fleets': fleets,
                'form': FleetSelectorForm(),
                'selected': None,
                'fleet_aircrafts': None,
            }
            return render(request, 'fleet/fleet.html', context)
    #If request method is other than "POST" (ie: "GET")

    
#View for update
def update(request):

    return HttpResponseRedirect(reverse('fleet_update'))

#View to delete
def destroy(request,):
    
    return HttpResponseRedirect(reverse('fleet_delete')) """