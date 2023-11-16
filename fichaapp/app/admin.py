from django.contrib import admin
from .models import Marca, Modelo, Camion

# Register your models here.

class CamionAdmin(admin.ModelAdmin):
    list_display = ["ppu","marca","modelo","anio"]
    list_editable = ["marca","modelo","anio"]
    search_fields = ["ppu"]
    list_filter = ["ppu","marca"]


admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Camion, CamionAdmin)


