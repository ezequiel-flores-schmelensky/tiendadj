from rest_framework.views import APIView
from firebase_admin import auth
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from .serializers import LoginSocialSerializer
from .models import Users

class LoginUser(TemplateView):
    template_name = "users/login.html"


class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_token = serializer.data.get('token_id')
        decoded_token = auth.verify_id_token(id_token)
        email = decoded_token['email']
        name = decoded_token['name']
        avatar = decoded_token['picture']
        verified = decoded_token['email_verified']
        usuario, created = User.objects.get_or_create(
            email = email,
            defaults = {
                'full_name': name,
                'email': email,
                'is_active': True
            }
        )
        return None