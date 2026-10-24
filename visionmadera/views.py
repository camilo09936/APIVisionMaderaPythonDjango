from django.shortcuts import render
from rest_framework import viewsets
from .models import (Usuario, EstadoCita, BloqueHorario, Sede, TipoPqrs, Calificacion, Disenador, AgendaDisenador, Cita)
from .serializers import(UsuarioSerializer, EstadoCitaSerializer, BloqueHorarioSerializer, SedeSerializer, TipoPqrsSerializer, CalificacionSerializer, DisenadorSerializer, AgendaDisenadorSerializer, CitaSerializer)
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
    queryset = TipoPqrs.objects.all()
    serializer_class = TipoPqrsSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class DisenadorViewSet(viewsets.ModelViewSet):
    queryset = Disenador.objects.all()
    serializer_class = DisenadorSerializer

class AgendaDisenadorViewSet(viewsets.ModelViewSet):
    queryset = AgendaDisenador.objects.all()
    serializer_class = AgendaDisenadorSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer