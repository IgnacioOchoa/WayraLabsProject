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
            general_results = []

            for acft in fleet_aircrafts:
                name = acft.aircraft.name
                landing_speed = acft.aircraft.landing_speed
                landing_distance = acft.aircraft.landing_distance
                quantity = acft.quantity
                acft_rot = rot(landing_speed, landing_distance, runway_length)
                results = {
                    'acft': name,
                    'landing_speed': landing_speed,
                    'breaking_time': acft_rot[0],
                    'taxiing_time': acft_rot[1],
                    'rot': round(acft_rot[0] + acft_rot[1], 2),
                    'quantity': quantity
                }
                general_results.append(results)
                total_operations += quantity
                average_rot += round(acft_rot[0] + acft_rot[1], 2)*quantity
            
            if total_operations == 0:
                average_rot = 0
                capacity = 0
            else:
                average_rot = round(average_rot / total_operations, 2)
                capacity = int(3600 / average_rot)

            context['average_rot'] = average_rot
            context['arrivals_per_hour'] = capacity
            context['general_results'] = general_results

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
    breaking_time = round((taxi_speed - speed)/acceleration, 2)
    taxiing_time = round(leftover_distance / taxi_speed, 2)
    return breaking_time, taxiing_time

def segment_length(n1, n2):
    segment_length = ((n1.x-n2.x)**2 + (n1.y-n2.y)**2)**0.5
    return segment_length