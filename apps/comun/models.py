from django.db import models

# Create your models here.
from apps.comun.vars import SEXO, HOMBRE
from apps.examen.models import Examen


class Paciente(models.Model):
    nombres = models.CharField('Nombres', max_length=50)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    fechaNacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO, default=HOMBRE)
    telefono = models.CharField(max_length=13, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)

class historiaPaciente(models.Model):
    paciente = models.ForeignKey(Paciente)
    fechaRegistro = models.DateTimeField()
    examen = models.ForeignKey(Examen)


class historiaPacienteDetalle(models.Model):
    historiapaciente = models.ForeignKey(historiaPaciente)
    nombreDetalle = models.CharField(max_length=30)
    referencia = models.CharField(max_length=100)
    resultado = models.CharField(max_length=100)
