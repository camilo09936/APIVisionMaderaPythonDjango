from django.shortcuts import render
from rest_framework import viewsets
from .models import (Usuario, EstadoCita, BloqueHorario, Sede)
from .serializers import(UsuarioSerializer, EstadoCitaSerializer, BloqueHorarioSerializer, SedeSerializer)
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