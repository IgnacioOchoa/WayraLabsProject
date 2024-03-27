from django.urls import path
from . import views

urlpatterns = [
        path('', views.geometryEdit, name="airport_edit"),
        path('update-node/<int:id>/', views.update_node, name="update_node"),
        path('delete-node/<int:id>/', views.delete_node, name="delete_node"),
        path('create-node/', views.create_node, name="create_node"),
        path('delete-link/<int:id>/', views.delete_link, name="delete_link")

]
