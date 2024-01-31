from django.shortcuts import render
from fleet.models import Fleet
from airport.models import Link, Node

# Create your views here.
def simulation(request):
    fleets = Fleet.objects.all()
    links = Link.objects.all()
    nodes = Node.objects.all()
    context={
        'fleets': fleets,
        'links': links,
        'nodes': nodes
    }    
    print(fleets)
    return render(request, 'simulation/simulation.html', context)
