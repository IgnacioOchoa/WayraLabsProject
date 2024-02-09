from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Fleet
from .models import AircraftQuantity
from .forms import FleetSelectorForm

# show view to display empty fleet page
def show(request):
    #fleet list and form for context
    fleets = Fleet.objects.all()

    context={
        'fleets': fleets,
    }
    return render(request, 'fleet/fleet.html', context)

#View to update fleet
def update(request, id):  
    fleet = Fleet.objects.get(id=id)
    fleet_aircrafts = AircraftQuantity.objects.filter(fleet = fleet).all()
    context={
        'fleet_aircrafts': fleet_aircrafts,
        'fleet': fleet,
    }

    return render(request, 'fleet/update.html', context)

#View to update fleet aircraft
def update_acft(request, fleet_acft_id):  
    fleet_aircraft = AircraftQuantity.objects.get(id=fleet_acft_id) 
    return render(request, 'fleet/update.html')    

# View to delete fleet
def destroy_fleet(request, id):  
    fleet = Fleet.objects.get(id=id)  
    # fleet.delete()  
    return render(request, 'fleet/delete.html', {'element': fleet})

# View to delete fleet
def destroy_acft(request, fleet_acft_id):
    fleet_aircraft = AircraftQuantity.objects.get(id=fleet_acft_id)   
     # fleet_aircraft.delete() 
    return render(request, 'fleet/delete.html', {'element': fleet_aircraft})

# View to create new fleet
def new_fleet(request):  
    return render(request, 'fleet/newfleet.html')



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