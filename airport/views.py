from django.shortcuts import render
from django.http import HttpResponse
from .models import Node, Link
from .forms import NodeForm

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
    node_form = NodeForm()
    context = { 'pointList' : pointList,
                'lineList' : lineList,
                'linkList' : linkList,
                'nodeList' : nodeList,
                'node_form': node_form } 

    return render(request, 'airport/drawing_component.html', context)
    #return HttpResponse('Hola mundo')

def update_node(request, node_id):  
    node = Node.objects.get(id=node_id)
    if request.method == "POST":
        form = NodeForm(request.POST, instance=node)
        if form.is_valid():
            try:  
                form.save()
                return HttpResponseRedirect(reverse('airport_edit'))  
            except:  
                pass



