from django import forms
from .models import Fleet, AircraftQuantity

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

class AcftForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control '
            self.fields[myField].widget.attrs['id'] = 'floatingInput'
            self.fields[myField].widget.attrs['placeholder'] = ''

    class Meta:
        model = AircraftQuantity
        exclude = ['fleet']

class AcftEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control '
            self.fields[myField].widget.attrs['id'] = 'floatingInput'
            self.fields[myField].widget.attrs['placeholder'] = ''

    class Meta:
        model = AircraftQuantity
        exclude = ['fleet', 'aircraft']