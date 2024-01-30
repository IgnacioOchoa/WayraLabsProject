from django.urls import path
from . import views

urlpatterns = [
        path('fleets/', views.fleets, name='fleets'),
]