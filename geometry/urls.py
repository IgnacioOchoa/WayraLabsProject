from django.urls import path
from . import views

urlpatterns = [
        path('geometry/', views.geometryEdit, name="geometry_edit")
]
