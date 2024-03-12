from django.urls import path
from . import views

urlpatterns = [
        path('airport/', views.geometryEdit, name="airport_edit"),
        path('airport/update-node/<int:id>', views.update_node, name="update_node")

]
