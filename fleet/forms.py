from django import forms
from .models import Fleet

class FleetSelectorForm(forms.Form):
    fleet_selector = forms.ModelChoiceField(queryset=Fleet.objects.all())