from django.shortcuts import render
from django.http import HttpResponse
from .models import Node, Link

# Create your views here.
def geometryEdit(request):
    pointList = []
    lineList = []
    linkList = []
    nodeList = []
    for n in Node.objects.all():
        pointList.append([n.x,n.y])
        nodeList.append(n)
    for l in Link.objects.all():
        lineList.append([l.node1.x, l.node1.y, l.node2.x, l.node2.y, l.width])
        linkList.append(l)
    context = { 'pointList' : pointList,
                'lineList' : lineList,
                'linkList' : linkList,
                'nodeList' : nodeList}
    return render(request, 'airport/drawing_component.html', context)
    #return HttpResponse('Hola mundo')
