from django.shortcuts import render
from fleet.models import Fleet, AircraftQuantity
from airport.models import Link, Node
from .forms import SimulationConfigForm

# Create your views here.
def simulation(request):
    #Context
    fleets = Fleet.objects.all()
    links = Link.objects.all()
    nodes = Node.objects.all()
    config_form = SimulationConfigForm()
    context={
        'fleets': fleets,
        'links': links,
        'nodes': nodes,
        'config_form': config_form,
    }
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        config_form = SimulationConfigForm(request.POST)
        # check whether it's valid:
        if config_form.is_valid():
            # process the data in form.cleaned_data as required
            selected_fleet = config_form.cleaned_data['fleet_selector']
            fleet_aircrafts = AircraftQuantity.objects.filter(fleet = selected_fleet).all()

            selected_runway = config_form.cleaned_data['runway_selector']
            print(selected_runway)

            #HARDCODED RUNWAY LENGTH... SHOULD BE GIVEN BY RUNWAY
            runway_length = 3000
            total_operations = 0
            average_rot = 0
            for acft in fleet_aircrafts:
                landing_speed = acft.aircraft.landing_speed
                landing_distance = acft.aircraft.landing_distance
                quantity = acft.quantity
                acft_rot = rot(landing_speed, landing_distance, runway_length)
                weighted_rot = acft_rot * quantity
                average_rot += weighted_rot
                total_operations += quantity
            
            if total_operations == 0:
                average_rot = 0
                capacity = 0
            else:
                average_rot = average_rot / total_operations
                capacity = int(3600 / average_rot)

            context['average_rot'] = average_rot
            context['arrivals_per_hour'] = capacity

            return render(request, 'simulation/simulation.html', context)
    else:
        return render(request, 'simulation/simulation.html', context)

def kt_to_ms(kt):
    return kt*0.514444

def rot(speed, distance, length):
    speed = kt_to_ms(speed)
    taxi_speed = kt_to_ms(20)
    #speed is landing speed, distance is landing distance, length is runway length
    acceleration = -(speed**2)/(2*distance)
    breaking_distance = ((taxi_speed**2)-(speed**2))/(2*acceleration)
    leftover_distance = length - breaking_distance
    breaking_time = (taxi_speed - speed)/acceleration
    taxiing_time = leftover_distance / taxi_speed
    rot = breaking_time + taxiing_time
    return rot

def segment_length(n1, n2):
    segment_length = ((n1.x-n2.x)**2 + (n1.y-n2.y)**2)**0.5
    return segment_length