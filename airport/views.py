from django.shortcuts import render
from django.http import HttpResponse
from .models import Node, Link

# Create your views here.
def geometryEdit(request):
    nodeList = []
    lineList = []
    for n in Node.objects.all():
        nodeList.append([n.x,n.y])
    for l in Link.objects.all():
        lineList.append([l.node1.x, l.node1.y, l.node2.x, l.node2.y])
    context = { 'nodeList' : nodeList,
                'lineList' : lineList}
    return render(request, 'airport/drawing_component.html', context)
    #return HttpResponse('Hola mundo')
