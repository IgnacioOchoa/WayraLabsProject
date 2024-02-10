from django.urls import path
from . import views

urlpatterns = [
        path('fleets/', views.show, name='fleets'),
        path('create/', views.create_fleet, name='create_fleet'),
        path('update/<int:id>', views.update_fleet, name='update_fleet'),
        path('delete/<int:id>', views.destroy_fleet, name='delete_fleet'),
        path('update/update/<int:fleet_acft_id>/', views.update_acft, name='acft_update'),
        path('update/delete/<int:fleet_acft_id>/', views.destroy_acft, name='acft_delete'),
        path('update/acft_details/<int:fleet_acft_id>/', views.details_acft, name='acft_details'),
]