from django.test import TestCase
from rest_framework.test import APIClient

from .models import Usuario, TipoPqrs, Pqrs


class PqrsModelTests(TestCase):
    def test_crear_tipo_y_pqrs(self):
        usuario = Usuario.objects.create(
            documento='123456789',
            nombre1='Ana',
            apellido1='García',
            correo='ana@example.com',
            contrasena='secret',
            direccion='Calle 1',
            telefono='3000000000',
            fecha_nacimiento='1990-01-15',
        )
        tipo, _ = TipoPqrs.objects.get_or_create(nombre='Queja')
        pqrs = Pqrs.objects.create(
            usuario=usuario,
            tipo_pqrs=tipo,
            descripcion='El servicio tuvo retrasos y no hubo respuesta.',
        )

        self.assertEqual(str(tipo), 'Queja')
        self.assertEqual(pqrs.usuario, usuario)
        self.assertEqual(pqrs.tipo_pqrs, tipo)
        self.assertEqual(pqrs.descripcion, 'El servicio tuvo retrasos y no hubo respuesta.')


class PqrsJwtTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = Usuario.objects.create(
            documento='987654321',
            nombre1='Luis',
            apellido1='Pérez',
            correo='luis@example.com',
            contrasena='secret123',
            direccion='Carrera 10',
            telefono='3001112233',
            fecha_nacimiento='1995-02-12',
        )

    def test_obtener_token_con_email_y_password(self):
        response = self.client.post('/api/token/', {'email': 'luis@example.com', 'password': 'secret123'}, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_usuarios_son_publicos_y_pqrs_requieren_token(self):
        usuarios_response = self.client.get('/api/usuarios/')
        self.assertEqual(usuarios_response.status_code, 200)

        pqrs_response = self.client.get('/api/pqrs/')
        self.assertEqual(pqrs_response.status_code, 401)

    def test_pqrs_acepta_token_valido(self):
        login_response = self.client.post('/api/token/', {'email': 'luis@example.com', 'password': 'secret123'}, format='json')
        self.assertEqual(login_response.status_code, 200)
        access_token = login_response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        pqrs_response = self.client.get('/api/pqrs/')
        self.assertEqual(pqrs_response.status_code, 200)
