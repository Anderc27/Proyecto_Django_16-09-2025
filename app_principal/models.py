from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('administrador', 'Administrador'),
        ('candidato', 'Candidato'),
    )
    rol = models.CharField(max_length=20, choices=ROLES, null=True, blank=True)

class Pregunta(models.Model):
    texto = models.CharField(max_length=255)
    opcion_a = models.CharField(max_length=255)
    opcion_b = models.CharField(max_length=255)
    opcion_c = models.CharField(max_length=255)
    respuesta_correcta = models.CharField(max_length=1, choices=(('a','A'),('b','B'),('c','C')))

    def __str__(self):
        return self.texto

class Resultado(models.Model):
    candidato = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)
    presentado = models.BooleanField(default=False)
