from django.contrib import admin

# Register your models here.
from .models import Fleet
from .models import Aircraft
from .models import AircraftQuantity

admin.site.register(Fleet)
admin.site.register(Aircraft)
admin.site.register(AircraftQuantity)