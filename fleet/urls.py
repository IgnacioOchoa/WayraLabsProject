from django.urls import path
from . import views

urlpatterns = [
        path('fleets/', views.fleets, name="fleets"),
        path('fleets/get_fleet', views.get_fleet, name="get_fleet")
]