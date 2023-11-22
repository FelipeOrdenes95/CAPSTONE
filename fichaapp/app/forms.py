from django import forms
from .models import ExteriorCamion, InteriorCamion, ElectronicaSeguridad, SuspensionFrenos, Motor, Llantas, Escaner, Fotos, Camion
from django.forms import inlineformset_factory
from django.db import models

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ["ppu", "marca", "modelo", "anio", "revision_tecnica","permiso_circulacion","soap","km", "ultima_inspeccion","proxima_inspeccion", "imagen","estado"]

    def as_text(self):
        estado = self.cleaned_data.get('estado')
        if estado is True:
            return '✅' 
        elif estado is False:
            return '❌' 
        else:
            return 'Por definir'  # Opción para estado desconocido

    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        if estado is None:  # Si el estado es desconocido
            return None  # Permite que el campo estado sea nulo en la base de datos
        return estado


class ExteriorCamionForm(forms.ModelForm):
    class Meta:
        model = ExteriorCamion
        fields = "__all__"

ExteriorCamionFormSet = inlineformset_factory(
    Camion,
    ExteriorCamion,
    fields="__all__",
    extra=1
)

class InteriorCamionForm(forms.ModelForm):
    class Meta:
        model = InteriorCamion
        fields = "__all__"

InteriorCamionFormSet = inlineformset_factory(
    Camion,
    InteriorCamion,
    fields="__all__",
    extra=1
)

class ElectronicaSeguridadForm(forms.ModelForm):
    class Meta:
        model = ElectronicaSeguridad
        fields = "__all__"

ElectronicaSeguridadFormSet = inlineformset_factory(
    Camion,
    ElectronicaSeguridad,
    fields="__all__",
    extra=1
)

class SuspensionFrenosForm(forms.ModelForm):
    class Meta:
        model = SuspensionFrenos
        fields = "__all__"

SuspensionFrenosFormSet = inlineformset_factory(
    Camion,
    SuspensionFrenos,
    fields="__all__",
    extra=1
)

class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = "__all__"

MotorFormSet = inlineformset_factory(
    Camion,
    Motor,
    fields="__all__",
    extra=1
)

class LlantasForm(forms.ModelForm):
    class Meta:
        model = Llantas
        fields = "__all__"

LlantasFormSet = inlineformset_factory(
    Camion,
    Llantas,
    fields="__all__",
    extra=1
)

class EscanerForm(forms.ModelForm):
    class Meta:
        model = Escaner
        fields = "__all__"

EscanerFormSet = inlineformset_factory(
    Camion,
    Escaner,
    fields="__all__",
    extra=1
)

class FotosForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = "__all__"

FotosFormSet = inlineformset_factory(
    Camion,
    Fotos,
    fields="__all__",
    extra=1
)

class NuevoCamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ["ppu", "marca", "modelo", "anio", "ultima_inspeccion","estado"]

    def __init__(self, *args, **kwargs):
        super(NuevoCamionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'required': 'required'})

