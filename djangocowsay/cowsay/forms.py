from django import forms
from cowsay.models import InputText

class InputTextForm(forms.Form):
    text = forms.CharField(max_length=200)

    def __str__(self):
        return self.text