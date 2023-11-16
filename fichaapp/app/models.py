from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Camion(models.Model):
    ppu = models.CharField(max_length=6)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, limit_choices_to={'marca': models.F('marca')})
    anio = models.IntegerField()
    ultima_inspeccion = models.DateField()
    imagen = models.ImageField(upload_to='camion_fotos/', null=True, blank=True)

    
    def __str__(self):
        return self.ppu
