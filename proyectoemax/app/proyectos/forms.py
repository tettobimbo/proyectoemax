from django import forms
from .models import proyecto

class proyectoform(forms.ModelForm):
    class Meta:
        model = proyecto
        fields = '__all__'
