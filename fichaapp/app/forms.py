from django import forms
from .models import ExteriorCamion, InteriorCamion, ElectronicaSeguridad, SuspensionFrenos, Motor, Llantas, Escaner, Fotos, Camion



class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ["ppu", "marca", "modelo", "anio", "ultima_inspeccion"]

    def __init__(self, *args, **kwargs):
        super(CamionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'required': 'required'})

class ExteriorCamionForm(forms.ModelForm):
    class Meta:
        model = ExteriorCamion
        fields = "__all__"

class InteriorCamionForm(forms.ModelForm):
    class Meta:
        model = InteriorCamion
        fields = "__all__"

class ElectronicaSeguridadForm(forms.ModelForm):
    class Meta:
        model = ElectronicaSeguridad
        fields = "__all__"

class SuspensionFrenosForm(forms.ModelForm):
    class Meta:
        model = SuspensionFrenos
        fields = "__all__"


class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = "__all__"


class LlantasForm(forms.ModelForm):
    class Meta:
        model = Llantas
        fields = "__all__"

class EscanerForm(forms.ModelForm):
    class Meta:
        model = Escaner
        fields = "__all__"

class FotosForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = "__all__"

class NuevoCamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ["ppu", "marca", "modelo", "anio", "ultima_inspeccion"]

    def __init__(self, *args, **kwargs):
        super(NuevoCamionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'required': 'required'})