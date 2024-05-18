from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, verbose_name='RUT', primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    estado =  models.BooleanField(default=True, verbose_name='Activo')
    creado_el = models.DateField(auto_now_add=True, verbose_name='Creado el', blank=True, null=True)
    actualizado_el = models.DateField(auto_now=True, verbose_name='Actualizado el')
    creado_por = models.CharField(max_lengt=50, verbose_name='Creado por')

    def __eq__(self, other):
        return self.rut == other.rut
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Address(models.Model):
    calle = models.CharField(max_length=50, verbose_name='Calle')
    numero = models.CharField(max_length=10, verbose_name='Número')
    dept = models.CharField(max_length=5, verbose_name='Departamento')
    comuna = models.CharField(max_length=50, verbose_name='Comuna')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')
    region = models.CharField(max_length=50, verbose_name='Estado')
    student = models.CharField(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante')

    def __str__(self):
        return f'{self.calle} {self.numero}, {self.region}'
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, verbose_name='RUT', primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    estado = models.BooleanField(default=True, verbose_name='Activo')
    creado_el = models.DateField(auto_now_add=True, verbose_name='Creado el', blank=True, null=True)
    actualizado_el = models.DateField(auto_now=True, verbose_name='Actualizado el')
    creado_por = models.CharField(max_lengt=50, verbose_name='Creado por')


    def __eq__(self, other):
        return self.rut == other.rut
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Curso(models.Model):
    codigo = models.CharField(max_length=10, verbose_name='Codigo', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')
    version = models.IntegerField(verbose_name='Version')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, verbose_name='Profesor', blank=True, null=True)

    def __eq__(self, other):
        return self.code == other.code
    
    def __str__(self):
        return f'{self.name}'
    
class Enrollment(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    creado_el = models.DateField(auto_now_add=True, verbose_name='Creado el')
    actualizado_el = models.DateField(auto_now=True, verbose_name='Actualizado el')
    creado_por = models.CharField(max_length=50, verbose_name='Creado por')
    
