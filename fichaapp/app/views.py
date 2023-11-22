from django.shortcuts import render, get_object_or_404, redirect
from .models import Camion, ExteriorCamion, InteriorCamion, ElectronicaSeguridad, SuspensionFrenos, Motor, Llantas, Escaner, Fotos
from .forms import (
    CamionForm,
    ExteriorCamionForm,
    InteriorCamionForm,
    ElectronicaSeguridadForm,
    SuspensionFrenosForm,
    MotorForm,
    LlantasForm,
    EscanerForm,
    FotosForm,
)
from django.forms import modelformset_factory, inlineformset_factory

from django.contrib import messages

ExteriorCamionFormSet = modelformset_factory(ExteriorCamion, form=ExteriorCamionForm, extra=1)
InteriorCamionFormSet = modelformset_factory(InteriorCamion, form=InteriorCamionForm, extra=1)
ElectronicaSeguridadFormSet = modelformset_factory(ElectronicaSeguridad, form=ElectronicaSeguridadForm, extra=1)
SuspensionFrenosFormSet = modelformset_factory(SuspensionFrenos, form=SuspensionFrenosForm, extra=1)
MotorFormSet = modelformset_factory(Motor, form=MotorForm, extra=1)
LlantasFormSet = modelformset_factory(Llantas, form=LlantasForm, extra=1)
EscanerFormSet = modelformset_factory(Escaner, form=EscanerForm, extra=1)
FotosFormSet = modelformset_factory(Fotos, form=FotosForm, extra=1)




def home(request):
    return render(request, 'app/home.html')

def tutorial(request):
    return render(request, 'app/tutorial.html')
    
def vehiculos(request):
    camiones = Camion.objects.all()

    # Procesa la búsqueda si se envía el formulario
    search_query = request.GET.get('search')
    if search_query:
        camiones = camiones.filter(ppu__icontains=search_query)

    return render(request, 'app/vehiculos.html', {'camiones': camiones})


def nuevo_camion(request):
    camion_form = CamionForm()
    ExteriorCamionFormSet = inlineformset_factory(Camion, ExteriorCamion, form=ExteriorCamionForm, fields="__all__", extra=1)
    InteriorCamionFormSet = inlineformset_factory(Camion, InteriorCamion, form=InteriorCamionForm, fields="__all__", extra=1)
    ElectronicaSeguridadFormSet = inlineformset_factory(Camion, ElectronicaSeguridad, form=ElectronicaSeguridadForm, fields="__all__", extra=1)
    SuspensionFrenosFormSet = inlineformset_factory(Camion, SuspensionFrenos, form=SuspensionFrenosForm, fields="__all__", extra=1)
    MotorFormSet = inlineformset_factory(Camion, Motor, form=MotorForm, fields="__all__", extra=1)
    LlantasFormSet = inlineformset_factory(Camion, Llantas, form=LlantasForm, fields="__all__", extra=1)
    EscanerFormSet = inlineformset_factory(Camion, Escaner, form=EscanerForm, fields="__all__", extra=1)
    FotosFormSet = inlineformset_factory(Camion, Fotos, form=FotosForm, fields="__all__", extra=1)

    exterior_formset = None
    interior_formset = None
    electronica_formset = None
    suspension_formset = None
    motor_formset = None
    llantas_formset = None
    escaner_formset = None
    fotos_formset = None

    if request.method == 'POST':
        camion_form = CamionForm(request.POST, request.FILES)
        exterior_formset = ExteriorCamionFormSet(request.POST, request.FILES, instance=Camion())
        interior_formset = InteriorCamionFormSet(request.POST, request.FILES, instance=Camion())
        electronica_formset = ElectronicaSeguridadFormSet(request.POST, request.FILES, instance=Camion())
        suspension_formset = SuspensionFrenosFormSet(request.POST, request.FILES, instance=Camion())
        motor_formset = MotorFormSet(request.POST, request.FILES, instance=Camion())
        llantas_formset = LlantasFormSet(request.POST, request.FILES, instance=Camion())
        escaner_formset = EscanerFormSet(request.POST, request.FILES, instance=Camion())
        fotos_formset = FotosFormSet(request.POST, request.FILES, instance=Camion())

        if (
            camion_form.is_valid() and exterior_formset.is_valid() and interior_formset.is_valid() and 
            electronica_formset.is_valid() and suspension_formset.is_valid() and motor_formset.is_valid() and 
            llantas_formset.is_valid() and escaner_formset.is_valid() and fotos_formset.is_valid()
        ):
            nuevo_camion = camion_form.save(commit=False)
            nuevo_camion.save()

            exterior_formset.instance = nuevo_camion
            exterior_formset.save()

            interior_formset.instance = nuevo_camion
            interior_formset.save()

            electronica_formset.instance = nuevo_camion
            electronica_formset.save()

            suspension_formset.instance = nuevo_camion
            suspension_formset.save()

            motor_formset.instance = nuevo_camion
            motor_formset.save()

            llantas_formset.instance = nuevo_camion
            llantas_formset.save()

            escaner_formset.instance = nuevo_camion
            escaner_formset.save()

            fotos_formset.instance = nuevo_camion
            fotos_formset.save()

            return redirect('listar_camion')
            # Procesar los datos del formulario
           
    else:
        camion_form = CamionForm()
        exterior_formset = ExteriorCamionFormSet(instance=Camion())
        interior_formset = InteriorCamionFormSet(instance=Camion())
        electronica_formset = ElectronicaSeguridadFormSet(instance=Camion())
        suspension_formset = SuspensionFrenosFormSet(instance=Camion())
        motor_formset = MotorFormSet(instance=Camion())
        llantas_formset = LlantasFormSet(instance=Camion())
        escaner_formset = EscanerFormSet(instance=Camion())
        fotos_formset = FotosFormSet(instance=Camion())

    return render(
        request,
        'app/camion/nuevo.html',
        {
            'camion_form': camion_form,
            'exterior_formset': exterior_formset,
            'interior_formset': interior_formset,
            'electronica_formset': electronica_formset,
            'suspension_formset': suspension_formset,
            'motor_formset': motor_formset,
            'llantas_formset': llantas_formset,
            'escaner_formset': escaner_formset,
            'fotos_formset': fotos_formset,
        }
    )

def listar_camion(request):
    camiones = Camion.objects.all()

    data = {
        'camiones': camiones  # Corregido el nombre de la variable
    }
    return render(request, 'app/camion/listar.html', data)


from django.shortcuts import redirect

from django.shortcuts import redirect



def modificar_camion(request, camion_id):
    camion = get_object_or_404(Camion, pk=camion_id)
    
    if request.method == 'POST':
        form = CamionForm(request.POST, instance=camion)
        if form.is_valid():
            form.save()
            return redirect('informe_vehiculo', camion_id=camion.id)
    else:
        form = CamionForm(instance=camion)
    
    return render(request, 'app/modificar_camion.html', {'form': form, 'camion': camion})
    
def eliminar_camion(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)
    camion.delete()
    return redirect('listar_camion')

def informe_vehiculo(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)
    return render(request, 'app/informe_vehiculo.html', {'camion': camion})


def vista_crear_camion(request):


    if request.method == 'POST':
        form = NuevoCamionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Camión creado exitosamente")
            return redirect('listar_camion')  # Redirige a la página de listar_camion después de guardar
    else:
        form = NuevoCamionForm()
    return render(request, 'nuevo.html', {'form': form})

def editar_ficha_camion(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)

    ExteriorCamionFormSet = inlineformset_factory(Camion, ExteriorCamion, form=ExteriorCamionForm, extra=1)
    InteriorCamionFormSet = inlineformset_factory(Camion, InteriorCamion, form=InteriorCamionForm, extra=1)
    ElectronicaSeguridadFormSet = inlineformset_factory(Camion, ElectronicaSeguridad, form=ElectronicaSeguridadForm, extra=1)
    SuspensionFrenosFormSet = inlineformset_factory(Camion, SuspensionFrenos, form=SuspensionFrenosForm, extra=1)
    MotorFormSet = inlineformset_factory(Camion, Motor, form=MotorForm, extra=1)
    LlantasFormSet = inlineformset_factory(Camion, Llantas, form=LlantasForm, extra=1)
    EscanerFormSet = inlineformset_factory(Camion, Escaner, form=EscanerForm, extra=1)
    FotosFormSet = inlineformset_factory(Camion, Fotos, form=FotosForm, extra=1)

    if request.method == 'POST':
        camion_form = CamionForm(request.POST, request.FILES, instance=camion)
        exterior_formset = ExteriorCamionFormSet(request.POST, request.FILES, instance=camion)
        interior_formset = InteriorCamionFormSet(request.POST, request.FILES, instance=camion)
        electronica_formset = ElectronicaSeguridadFormSet(request.POST, request.FILES, instance=camion)
        suspension_formset = SuspensionFrenosFormSet(request.POST, request.FILES, instance=camion)
        motor_formset = MotorFormSet(request.POST, request.FILES, instance=camion)
        llantas_formset = LlantasFormSet(request.POST, request.FILES, instance=camion)
        escaner_formset = EscanerFormSet(request.POST, request.FILES, instance=camion)
        fotos_formset = FotosFormSet(request.POST, request.FILES, instance=camion)

        if (
            camion_form.is_valid() and exterior_formset.is_valid() and interior_formset.is_valid() and
            electronica_formset.is_valid() and suspension_formset.is_valid() and motor_formset.is_valid() and
            llantas_formset.is_valid() and escaner_formset.is_valid() and fotos_formset.is_valid()
        ):
            camion_form.save()
            exterior_formset.save()
            interior_formset.save()
            electronica_formset.save()
            suspension_formset.save()
            motor_formset.save()
            llantas_formset.save()
            escaner_formset.save()
            fotos_formset.save()

            return redirect('informe_vehiculo', camion_id=camion.id)

    else:
        camion_form = CamionForm(instance=camion)
        exterior_formset = ExteriorCamionFormSet(instance=camion)
        interior_formset = InteriorCamionFormSet(instance=camion)
        electronica_formset = ElectronicaSeguridadFormSet(instance=camion)
        suspension_formset = SuspensionFrenosFormSet(instance=camion)
        motor_formset = MotorFormSet(instance=camion)
        llantas_formset = LlantasFormSet(instance=camion)
        escaner_formset = EscanerFormSet(instance=camion)
        fotos_formset = FotosFormSet(instance=camion)

    return render(
        request,
        'app/editar_ficha_camion.html',
        {
            'camion_form': camion_form,
            'exterior_formset': exterior_formset,
            'interior_formset': interior_formset,
            'electronica_formset': electronica_formset,
            'suspension_formset': suspension_formset,
            'motor_formset': motor_formset,
            'llantas_formset': llantas_formset,
            'escaner_formset': escaner_formset,
            'fotos_formset': fotos_formset,
            'camion': camion,
        }
    )

def buscar_camion(request):
    query = request.GET.get('query', '')
    
   
    camiones = Camion.objects.filter(ppu__icontains=query)
    
    return render(request, 'app/busqueda_resultados.html', {'camiones': camiones})  