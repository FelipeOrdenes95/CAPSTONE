from django.shortcuts import render, redirect, get_object_or_404
from .models import Camion
from .forms import CamionForm
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
    if request.method == 'POST':
        formulario = CamionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente")
            return redirect(to="listar_camion")
        else:
            messages.error(request, "Hubo un error en el formulario")

    return render(request, 'app/camion/nuevo.html', {'form': CamionForm()})

def listar_camion(request):
    camiones = Camion.objects.all()

    data = {
        'camiones': camiones  # Corregido el nombre de la variable
    }
    return render(request, 'app/camion/listar.html', data)


def modificar_camion(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)
    
    data = {
        'form': CamionForm(instance=camion)
    }

    if request.method == 'POST':
        formulario = CamionForm(data=request.POST, files=request.FILES, instance=camion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_camion")
            data["mensaje"] = "Modificado con Éxito"
        else:
            data["form"] = formulario

    return render(request, 'app/camion/modificar.html', data)


def eliminar_camion(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)
    camion.delete()
    return redirect('listar_camion')

def informe_vehiculo(request, camion_id):
    camion = get_object_or_404(Camion, pk=camion_id)
    return render(request, 'app/informe_vehiculo.html', {'camion': camion})