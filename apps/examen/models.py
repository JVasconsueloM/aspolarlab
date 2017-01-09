from django.db import models

# Create your models here.
from django.urls import reverse

from apps.examen.vars import EXAMEN_TIPOPARAM


class Examen(models.Model):
    nombre = models.CharField('Nombre', max_length=30)

    def __str__(self):
        return self.nombre


class Referencia(models.Model):
    nombre = models.CharField('Nombre', max_length=30)


class ExamenParametros(models.Model):
    examen = models.ForeignKey(Examen)
    tipo = models.CharField('Tipo', max_length=1, choices=EXAMEN_TIPOPARAM)
    nombre = models.CharField('Nombre', max_length=30)
    referenciaInicial = models.DecimalField('Valor Inicial', max_digits=5, decimal_places=2, null=True, blank=True)
    referenciaFinal = models.DecimalField('Valor Final', max_digits=5, decimal_places=2, null=True, blank=True)
    referenciaTextual = models.ManyToManyField(Referencia)
    edadInicio = models.SmallIntegerField()
    edadTermino = models.SmallIntegerField()
