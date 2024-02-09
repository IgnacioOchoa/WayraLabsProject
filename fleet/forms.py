from django import forms
from .models import Fleet

class FleetSelectorForm(forms.Form):
    fleet_selector = forms.ModelChoiceField(label="Choose fleet", queryset=Fleet.objects.all(), widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

class FleetForm(forms.ModelForm):
    class Meta:
        model = Fleet
        fields = "__all__"