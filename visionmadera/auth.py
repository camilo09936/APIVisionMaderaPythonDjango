from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Usuario


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get('user_id') or validated_token.get('documento')
        if not user_id:
            return None

        try:
            return Usuario.objects.get(documento=user_id)
        except Usuario.DoesNotExist:
            return None
