from django import forms
from .models import comps

class ProductEditform(forms.ModelForm):
    class Meta:
        model = comps
        exclude = ['owner']