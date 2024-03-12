from django import forms
from .models import Node, Link

class NodeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control '
            self.fields[myField].widget.attrs['id'] = 'floatingInput'
            self.fields[myField].widget.attrs['placeholder'] = ''

    class Meta:
        model = Node
        fields = ['x','y']

class LinkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control '
            self.fields[myField].widget.attrs['id'] = 'floatingInput'
            self.fields[myField].widget.attrs['placeholder'] = ''

    class Meta:
        model = Link
        fields = ['node1','node2']

