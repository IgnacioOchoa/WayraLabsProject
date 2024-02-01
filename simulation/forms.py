from django import forms
from fleet.models import Fleet
from airport.models import Link
from airport.models import Node

class SimulationConfigForm(forms.Form):
    fleet_selector = forms.ModelChoiceField(label="Choose fleet", queryset=Fleet.objects.all())
    fleet_selector.widget.attrs.update({"class": "formsize"})

    runway_selector = forms.ModelChoiceField(label="Choose runway", queryset=Link.objects.all())
    runway_selector.widget.attrs.update({"class": "formsize"})

    threshold_selector = forms.ModelChoiceField(label="Choose threshold", queryset=Node.objects.all())
    threshold_selector.widget.attrs.update({"class": "formsize"})
    