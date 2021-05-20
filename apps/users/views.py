from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from .models import User

# Create your views here.
class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = ()


class CurrentUser(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        user = get_object_or_404(User, username=request.user.username)
        data = UserSerializer(user).data
        return Response(data)


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token" : user.auth_token.key})
        else:
            return Response({"error" : "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

