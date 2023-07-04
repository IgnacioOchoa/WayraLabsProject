from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def geometryEdit(request):
    context = {}
    return render(request, 'geometry/drawing_component.html', context)
    #return HttpResponse('Hola mundo')
