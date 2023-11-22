from django.db import models


OPCIONES = [
    ('ok', 'Ok'),
    ('con_detalle', 'Con Detalle'),
    ('na', 'N/A'),
]

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
    estado = models.BooleanField(null=True)
    proxima_inspeccion = models.DateField(null=True, blank=True)
    revision_tecnica = models.DateField(null=True, blank=True)
    permiso_circulacion = models.DateField(null=True, blank=True)
    soap = models.DateField(null=True, blank=True)
    km = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.ppu


   

class ExteriorCamion(models.Model):
    camion = models.OneToOneField('Camion', on_delete=models.CASCADE, primary_key=True)
    puertas = models.CharField(max_length=20, choices=OPCIONES, default='na')
    espejos = models.CharField(max_length=20, choices=OPCIONES, default='na')
    ventanas = models.CharField(max_length=20, choices=OPCIONES, default='na')
    focos = models.CharField(max_length=20, choices=OPCIONES, default='na')
    parachoques = models.CharField(max_length=20, choices=OPCIONES, default='na')
    capot = models.CharField(max_length=20, choices=OPCIONES, default='na')
    techo = models.CharField(max_length=20, choices=OPCIONES, default='na')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Exterior de {self.camion}"

class InteriorCamion(models.Model):
    camion = models.OneToOneField('Camion', on_delete=models.CASCADE, primary_key=True)
    tapiz = models.CharField(max_length=20, choices=OPCIONES, default='na')
    asientos = models.CharField(max_length=20, choices=OPCIONES, default='na')
    talero = models.CharField(max_length=20, choices=OPCIONES, default='na')
    cerradura = models.CharField(max_length=20, choices=OPCIONES, default='na')
    botones = models.CharField(max_length=20, choices=OPCIONES, default='na')
    limpiaparabrisas = models.CharField(max_length=20, choices=OPCIONES, default='na')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Interior de {self.camion}"

class ElectronicaSeguridad(models.Model):
    camion = models.OneToOneField('Camion', on_delete=models.CASCADE, primary_key=True)
    luces_testigos = models.CharField(max_length=20, choices=OPCIONES, default='na')
    airbags = models.CharField(max_length=20, choices=OPCIONES, default='na')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Electrónica y seguridad de {self.camion}"

class SuspensionFrenos(models.Model):
    camion = models.OneToOneField('Camion', on_delete=models.CASCADE, primary_key=True)
    direccion_funcionamiento = models.CharField(max_length=20, choices=OPCIONES, default='na')
    amortiguadores_condicion = models.CharField(max_length=20, choices=OPCIONES, default='na')
    frenos_estado = models.CharField(max_length=20, choices=OPCIONES, default='na')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Suspensión y frenos de {self.camion}"

class Motor(models.Model):
    camion = models.OneToOneField('Camion', on_delete=models.CASCADE, primary_key=True)
    condicion_motor = models.CharField(max_length=20, choices=OPCIONES, default='na')
    ruido_motor = models.CharField(max_length=20, choices=OPCIONES, default='na')
    cableado = models.CharField(max_length=20, choices=OPCIONES, default='na')
    condicion_bateria = models.CharField(max_length=20, choices=OPCIONES, default='na')
    humo_visible = models.CharField(max_length=20, choices=OPCIONES, default='na')
    mangueras_motor = models.CharField(max_length=20, choices=OPCIONES, default='na')
    condicion_carter_aceite = models.CharField(max_length=20, choices=OPCIONES, default='na')
    sistema_refrigeracion = models.CharField(max_length=20, choices=OPCIONES, default='na')
    condicion_transmision = models.CharField(max_length=20, choices=OPCIONES, default='na')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Información del motor de {self.camion}"

class Llantas(models.Model):
    camion = models.OneToOneField('Camion', on_delete=models.CASCADE, primary_key=True)
    condicion_neumaticos = models.CharField(max_length=20, choices=OPCIONES, default='na')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Información de llantas de {self.camion}"

class Escaner(models.Model):
    camion = models.OneToOneField('Camion', on_delete=models.CASCADE, primary_key=True)
    sistema_abs = models.CharField(max_length=20, choices=OPCIONES, default='na')
    ecu_transmision = models.CharField(max_length=20, choices=OPCIONES, default='na')
    ecu_airbag = models.CharField(max_length=20, choices=OPCIONES, default='na')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Información del escáner de {self.camion}"

class Fotos(models.Model):
    camion = models.OneToOneField('Camion', on_delete=models.CASCADE, primary_key=True)
    imagen1 = models.ImageField(upload_to='fotos/', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return f"Fotos de {self.camion}"
   

    
