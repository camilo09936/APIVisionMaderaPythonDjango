from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (Usuario, EstadoCita, BloqueHorario, Sede, TipoPqrs, Pqrs)
from .serializers import(UsuarioSerializer, EstadoCitaSerializer, BloqueHorarioSerializer, SedeSerializer, TipoPqrsSerializer, PqrsSerializer)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class= UsuarioSerializer
    permission_classes= [AllowAny]
    
class EstadoCitaViewSet(viewsets.ModelViewSet):
    queryset= EstadoCita.objects.all()
    serializer_class= EstadoCitaSerializer
    permission_classes= [AllowAny]
    
class BloqueHorarioViewSet(viewsets.ModelViewSet):
    queryset= BloqueHorario.objects.all()
    serializer_class= BloqueHorarioSerializer
    permission_classes= [AllowAny]
    
class SedeViewSet(viewsets.ModelViewSet):
    queryset= Sede.objects.all()
    serializer_class= SedeSerializer
    permission_classes= [AllowAny]

class TipoPqrsViewSet(viewsets.ModelViewSet):
    queryset= TipoPqrs.objects.all()
    serializer_class= TipoPqrsSerializer
    permission_classes= [IsAuthenticated]

class PqrsViewSet(viewsets.ModelViewSet):
    queryset= Pqrs.objects.all()
    serializer_class= PqrsSerializer
    permission_classes= [IsAuthenticated]


class UsuarioTokenObtainPairView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email') or request.data.get('correo')
        password = request.data.get('password')

        if not email or not password:
            return Response({'detail': 'Debe enviar email y password'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = Usuario.objects.get(correo=email)
        except Usuario.DoesNotExist:
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        if usuario.contrasena != password:
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken()
        refresh['user_id'] = usuario.documento
        refresh['documento'] = usuario.documento
        refresh['correo'] = usuario.correo

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'usuario': {
                'documento': usuario.documento,
                'correo': usuario.correo,
                'nombre': f"{usuario.nombre1} {usuario.apellido1}".strip(),
            },
        }, status=status.HTTP_200_OK)