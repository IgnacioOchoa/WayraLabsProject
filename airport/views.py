from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Node, Link
from .forms import NodeForm, LinkForm

# Create your views here.
def geometryEdit(request):
    nodeListSerial = []
    linkListSerial = []
    for n in Node.objects.all():
        nodeListSerial.append({'type':n.Type.labels[int(n.type)-1], 'x':n.x, 'y':n.y, 'z':n.z})
    for l in Link.objects.all():
        linkListSerial.append({'type': l.type, 'node1name': l.node1.__str__(), 'node2name': l.node2.__str__(), 'node1x': l.node1.x, 'node1y': l.node1.y, 'node2x': l.node2.x, 'node2y': l.node2.y, 'width':l.width})
    node_form = NodeForm()
    link_form = LinkForm()
    context = { 'nodeListSerial' : nodeListSerial,
                'linkListSerial' : linkListSerial,
                'linkList' : list(Link.objects.all()),
                'nodeList' : list(Node.objects.all()),
                'node_form': node_form,
                'link_form': link_form } 

    return render(request, 'airport/drawing_component.html', context)
    #return HttpResponse('Hola mundo')

def update_node(request, id):  
    print('Update node being executed')
    print('Post = ' + str(request.POST))
    node = Node.objects.get(id=id)
    if request.method == "POST":
      form = NodeForm(request.POST, instance=node) 
      if form.is_valid():
        try:  
            form.save()
            return HttpResponseRedirect(reverse('airport_edit'))  
        except:  
            pass
    return HttpResponseRedirect(reverse('airport_edit'))

def delete_node(request, id):
    node = Node.objects.get(id=id)
    node.delete()
    return HttpResponseRedirect(reverse('airport_edit'))

def create_node(request):
    if request.method == "POST":
        form = NodeForm(request.POST)
        if form.is_valid():
            new_node = form.save(commit=False)
            new_node.save()
            return HttpResponseRedirect(reverse('airport_edit'))

def delete_link(request, id):
    link = Link.objects.get(id=id)
    link.delete()
    return HttpResponseRedirect(reverse('airport_edit'))



