from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from django.contrib.auth.models import User

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TypeOfUser(viewsets.ModelViewSet):
    queryset = TypeOfUser.objects.all()
    serializer_class = TypeOfUserSerializer