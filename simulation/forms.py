from django import forms
from fleet.models import Fleet
from simulation.models import Runway

class SimulationConfigForm(forms.Form):
    fleet_selector = forms.ModelChoiceField(label="Choose fleet", queryset=Fleet.objects.all())
    fleet_selector.widget.attrs.update({"class": "formsize"})

    runway_selector = forms.ModelChoiceField(label="Choose runway", queryset=Runway.objects.all())
    runway_selector.widget.attrs.update({"class": "formsize"})
    