from django.shortcuts import render, redirect, get_object_or_404
from .models import Camion, ExteriorCamion, InteriorCamion, ElectronicaSeguridad, SuspensionFrenos, Motor, Llantas, Escaner, Fotos
from .forms import (
    CamionForm, 
    NuevoCamionForm, 
    ExteriorCamionForm, 
    InteriorCamionForm, 
    ElectronicaSeguridadForm, 
    SuspensionFrenosForm, 
    MotorForm, 
    LlantasForm, 
    EscanerForm, 
    FotosForm
)
from django.forms import inlineformset_factory
from django.contrib import messages



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
    camion = get_object_or_404(Camion, id=camion_id)

    ExteriorCamionFormSet = inlineformset_factory(Camion, ExteriorCamion, form=ExteriorCamionForm, fields="__all__", extra=0)
    InteriorCamionFormSet = inlineformset_factory(Camion, InteriorCamion, form=InteriorCamionForm, fields="__all__", extra=0)

    if request.method == 'POST':
        formulario = CamionForm(data=request.POST, files=request.FILES, instance=camion)
        exterior_formset = ExteriorCamionFormSet(request.POST, instance=camion)
        interior_formset = InteriorCamionFormSet(request.POST, instance=camion)

        if formulario.is_valid() and exterior_formset.is_valid() and interior_formset.is_valid():
            formulario.save()
            exterior_formset.save()
            interior_formset.save()
            messages.success(request, "Modificado con éxito")
            return redirect('informe_vehiculo', camion_id=camion_id)
        else:
            messages.error(request, "Hubo un error al modificar el camión")
    else:
        formulario = CamionForm(instance=camion)
        exterior_formset = ExteriorCamionFormSet(instance=camion)
        interior_formset = InteriorCamionFormSet(instance=camion)

    data = {
        'form': formulario,
        'exterior_formset': exterior_formset,
        'interior_formset': interior_formset,
    }

    return render(request, 'app/camion/modificar.html', data)


def eliminar_camion(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)
    camion.delete()
    return redirect('listar_camion')

def informe_vehiculo(request, camion_id):
    camion = get_object_or_404(Camion, pk=camion_id)
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