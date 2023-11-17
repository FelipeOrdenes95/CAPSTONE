from django.contrib import admin
from .models import Marca, Modelo, Camion, ExteriorCamion, InteriorCamion, ElectronicaSeguridad, SuspensionFrenos, Motor, Llantas, Escaner, Fotos

class ExteriorCamionInline(admin.StackedInline):
    model = ExteriorCamion
    max_num = 1

class InteriorCamionInline(admin.StackedInline):
    model = InteriorCamion
    max_num = 1

class ElectronicaSeguridadInline(admin.StackedInline):
    model = ElectronicaSeguridad
    max_num = 1

class SuspensionFrenosInline(admin.StackedInline):
    model = SuspensionFrenos
    max_num = 1

class MotorInline(admin.StackedInline):
    model = Motor
    max_num = 1

class LlantasInline(admin.StackedInline):
    model = Llantas
    max_num = 1

class EscanerInline(admin.StackedInline):
    model = Escaner
    max_num = 1

class FotosInline(admin.StackedInline):
    model = Fotos
    max_num = 1


class CamionAdmin(admin.ModelAdmin):
    list_display = ["ppu", "marca", "modelo", "anio"]
    list_editable = ["marca", "modelo", "anio"]
    search_fields = ["ppu"]
    list_filter = ["ppu", "marca"]
    inlines = [ExteriorCamionInline, InteriorCamionInline, ElectronicaSeguridadInline, SuspensionFrenosInline, MotorInline, LlantasInline, EscanerInline, FotosInline]

admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Camion, CamionAdmin)
