from django.shortcuts import render
from rest_framework import viewsets
from .models import (Usuario, EstadoCita, BloqueHorario, Sede, TipoPqrs, Pqrs, Calificacion, Disenador, AgendaDisenador, Cita, EstadoPqrs)
from .serializers import(UsuarioSerializer, EstadoCitaSerializer, BloqueHorarioSerializer, SedeSerializer, TipoPqrsSerializer, PqrsSerializer, CalificacionSerializer, DisenadorSerializer, AgendaDisenadorSerializer, CitaSerializer, EstadoPqrsSerializer)
from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class= UsuarioSerializer
    permission_classes= [IsAuthenticated]
    
class EstadoCitaViewSet(viewsets.ModelViewSet):
    queryset= EstadoCita.objects.all()
    serializer_class= EstadoCitaSerializer
    permission_classes= [IsAuthenticated]
    
class BloqueHorarioViewSet(viewsets.ModelViewSet):
    queryset= BloqueHorario.objects.all()
    serializer_class= BloqueHorarioSerializer
    permission_classes= [IsAuthenticated]
    
class SedeViewSet(viewsets.ModelViewSet):
    queryset= Sede.objects.all()
    serializer_class= SedeSerializer
    permission_classes= [IsAuthenticated]
    
class TipoPqrsViewSet(viewsets.ModelViewSet):
    queryset= TipoPqrs.objects.all()
    serializer_class= TipoPqrsSerializer
    permission_classes= [IsAuthenticated]
    
class EstadoPqrsViewSet(viewsets.ModelViewSet):
    queryset= EstadoPqrs.objects.all()
    serializer_class= EstadoPqrsSerializer
    permission_classes= [IsAuthenticated]
    
class PqrsViewSet(viewsets.ModelViewSet):
    queryset= Pqrs.objects.all()
    serializer_class= PqrsSerializer
    permission_classes= [IsAuthenticated]

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    permission_classes= [IsAuthenticated]
    
class DisenadorViewSet(viewsets.ModelViewSet):
    queryset = Disenador.objects.all()
    serializer_class = DisenadorSerializer
    permission_classes= [IsAuthenticated]
    
class AgendaDisenadorViewSet(viewsets.ModelViewSet):
    queryset = AgendaDisenador.objects.all()
    serializer_class = AgendaDisenadorSerializer
    permission_classes= [IsAuthenticated]

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes= [IsAuthenticated]