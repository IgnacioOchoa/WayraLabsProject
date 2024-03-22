from django.urls import path
from . import views

urlpatterns = [
        path('fleets/', views.show, name='fleets'),
        path('create/', views.create_fleet, name='create_fleet'),
        path('update_name/<int:id>', views.update_name, name='update_fleet_name'),
        path('update/<int:id>', views.update_fleet, name='update_fleet'),
        path('delete/<int:id>', views.destroy_fleet, name='destroy_fleet'),
        path('update/create/<int:id>', views.create_acft, name='create_acft'),
        path('update/update/<int:fleet_acft_id>', views.update_acft, name='update_acft'),
        path('update/delete/<int:fleet_acft_id>/', views.destroy_acft, name='destroy_acft'),
        path('update/acft_details/<int:fleet_acft_id>/', views.acft_details, name='acft_details'),
        path('update_db', views.update_db, name='update_db'),
]