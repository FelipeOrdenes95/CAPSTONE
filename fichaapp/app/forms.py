from django import forms
from .models import Camion


class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ["ppu", "marca", "modelo","anio","ultima_inspeccion", "imagen"]
