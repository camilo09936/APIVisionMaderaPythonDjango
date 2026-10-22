from django.shortcuts import render
from rest_framework import viewsets
from .models import (Usuario, EstadoCita, BloqueHorario, Sede, TipoPqrs, Pqrs)
from .serializers import(UsuarioSerializer, EstadoCitaSerializer, BloqueHorarioSerializer, SedeSerializer, TipoPqrsSerializer, PqrsSerializer)
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

class PqrsViewSet(viewsets.ModelViewSet):
    queryset= Pqrs.objects.all()
    serializer_class= PqrsSerializer
    permission_classes= [IsAuthenticated]