from rest_framework.views import APIView
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from .serializers import LoginSocialSerializer


class LoginUser(TemplateView):
    template_name = "users/login.html"


class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_token = serializer.data.get('token_id')

        return None