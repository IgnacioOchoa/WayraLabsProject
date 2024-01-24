from django.urls import path
from . import views

urlpatterns = [
        path('airport/', views.geometryEdit, name="geometry_edit")
]
