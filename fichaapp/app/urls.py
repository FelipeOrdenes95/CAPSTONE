from django.urls import path
from .views import home, tutorial, vehiculos, nuevo_camion, listar_camion, modificar_camion, eliminar_camion, informe_vehiculo, editar_ficha_camion, buscar_camion
from . import views


urlpatterns = [
    path('', home, name="home"),
    path('tutorial/', tutorial, name="tutorial"),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('nuevo-camion/', nuevo_camion, name="nuevo_camion"),
    path('listar-camion/', listar_camion, name="listar_camion"),
    path('modificar-camion/<int:camion_id>/', modificar_camion, name="modificar_camion"),
    path('eliminar-camion/<int:camion_id>/', eliminar_camion, name="eliminar_camion"),
    path('informe_vehiculo/<int:camion_id>/', informe_vehiculo, name='informe_vehiculo'),
    path('editar_ficha_camion/<int:camion_id>/', editar_ficha_camion, name='editar_ficha_camion'),
    path('buscar_camion/', views.buscar_camion, name='buscar_camion'),
]