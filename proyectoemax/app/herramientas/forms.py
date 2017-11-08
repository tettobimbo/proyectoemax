from django import forms
from .models import herramienta

class herramientasform(forms.ModelForm):
    class Meta:
        model = herramienta
        fields = '__all__'
