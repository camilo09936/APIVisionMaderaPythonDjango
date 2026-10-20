from django.db import models

class Usuario(models.Model):
    documento= models.CharField(max_length=30, primary_key=True)
    nombre1= models.CharField(max_length=100)
    nombre2= models.CharField(max_length=100, null=True, blank=True)
    apellido1= models.CharField(max_length=100)
    apellido2= models.CharField(max_length=100, null=True, blank=True)
    correo= models.EmailField(unique=True)
    contrasena= models.CharField(max_length=255)
    direccion= models.CharField(max_length=200)
    telefono= models.CharField(max_length=20)
    fecha_nacimiento= models.DateField()
    
    def __str__(self):
        return f"{self.nombre1} {self.nombre2} {self.apellido1} {self.apellido2} - ({self.documento})"

class EstadoCita(models.Model):
    id_estado_cita= models.AutoField(auto_created=True, primary_key=True)
    nombre= models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
class BloqueHorario(models.Model):
    id_bloque= models.AutoField(auto_created=True, primary_key=True)
    hora_inicio= models.TimeField()
    hora_fin= models.TimeField()
    
    def __str__(self):
        return f"{self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}"

class Sede(models.Model):
    id_sede= models.AutoField(auto_created=True, primary_key=True)
    nombre= models.CharField(max_length=100)
    direccion= models.CharField(max_length=200)
    telefono= models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre