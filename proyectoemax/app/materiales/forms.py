from django import forms
from .models import materiales

class materialesform(forms.ModelForm):
    class Meta:
        model = material
        fields = '__all__'
