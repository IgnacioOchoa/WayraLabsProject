from django import forms
from .models import Fleet

class FleetSelectorForm(forms.Form):
    fleet_selector = forms.ModelChoiceField(label="Choose fleet", queryset=Fleet.objects.all())