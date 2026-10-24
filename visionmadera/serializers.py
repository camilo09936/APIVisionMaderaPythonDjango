from rest_framework import serializers
from .models import (Usuario, EstadoCita, BloqueHorario, Sede, TipoPqrs, Calificacion)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields= '__all__'

class EstadoCitaSerializer(serializers.ModelSerializer):
    class Meta:
        model= EstadoCita
        fields= '__all__'
        
class BloqueHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= BloqueHorario
        fields= '__all__'
        
class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sede
        fields= '__all__'

class TipoPqrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPqrs
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'