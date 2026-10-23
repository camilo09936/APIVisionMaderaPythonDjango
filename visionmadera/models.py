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

class Disenador(models.Model):
    id_disenador= models.AutoField(auto_created=True, primary_key=True)
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    correo= models.EmailField(max_length=100, unique=True)
    sede= models.ForeignKey(Sede, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class AgendaDisenador(models.Model):
    id_agenda= models.AutoField(auto_created=True, primary_key=True)
    disenador= models.ForeignKey(Disenador, on_delete=models.PROTECT)
    dia_semana= models.CharField(max_length=20)
    bloque= models.ForeignKey(BloqueHorario, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.disenador} - {self.dia_semana} ({self.bloque})"

class Cita(models.Model):
    id_cita= models.AutoField(auto_created=True, primary_key=True)
    fecha= models.DateField()
    bloque= models.ForeignKey(BloqueHorario, on_delete=models.PROTECT)
    estado_cita= models.ForeignKey(EstadoCita, on_delete=models.PROTECT, default=1)
    usuario= models.ForeignKey(Usuario, on_delete=models.PROTECT)
    sede= models.ForeignKey(Sede, on_delete=models.PROTECT)
    disenador= models.ForeignKey(Disenador, on_delete=models.PROTECT)

    def __str__(self):
        return f"Cita {self.id_cita} - {self.fecha}"