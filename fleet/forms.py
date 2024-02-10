from django import forms
from .models import Fleet

class FleetSelectorForm(forms.Form):
    fleet_selector = forms.ModelChoiceField(label="Choose fleet", queryset=Fleet.objects.all(), widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

class FleetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control '
            self.fields[myField].widget.attrs['id'] = 'floatingInput'
            self.fields[myField].widget.attrs['placeholder'] = ''

    class Meta:
        model = Fleet
        fields = ['name']