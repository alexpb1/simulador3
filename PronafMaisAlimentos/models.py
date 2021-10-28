<<<<<<< HEAD
from datetime import datetime
from django.db import models
from django.forms.fields import DateField

class EntradasMaisAlimentos(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    divisao = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0)  
    carencia = models.PositiveIntegerField(default=0)
    taxa = models.DecimalField(max_digits=7, decimal_places=2, blank=False,default=0.0)
    dataPrimeiraParcela=models.DateField(default=datetime.now())
    def __str__(self):
        return self.valor
=======
from datetime import datetime
from django.db import models
from django.forms.fields import DateField

class EntradasMaisAlimentos(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    divisao = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0)  
    carencia = models.PositiveIntegerField(default=0)
    taxa = models.DecimalField(max_digits=7, decimal_places=2, blank=False,default=0.0)
    dataPrimeiraParcela=models.DateField(default=datetime.now())
    def __str__(self):
        return self.valor
>>>>>>> ff6a3c90b9141ef6edc7254235d24cf57f2487b3
