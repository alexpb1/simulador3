from typing import Tuple
from django import forms
from .models import *

class simulaForm(forms.ModelForm):
    class Meta:
        model = EntradasMaisAlimentos
        fields=('valor', 'divisao', 'carencia', 'taxa')
    def clean(self):
        return self.cleaned_data
    
     
