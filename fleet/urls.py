from django.urls import path
from . import views

urlpatterns = [
        path('fleets/', views.show, name='fleets'),
        path('newfleet/', views.new_fleet, name='new_fleet'),
        path('update/<int:id>', views.update, name='fleet_update'),
        path('delete/<int:id>', views.destroy_fleet, name='fleet_delete'),
        path('update/delete/<int:fleet_acft_id>/', views.destroy_acft, name='acft_delete'),
        path('update/update/<int:fleet_acft_id>/', views.update_acft, name='acft_update'),
]