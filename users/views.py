from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer

from rest_framework.generics import ListAPIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserListApiView(ListAPIView):# Lista todos los usuarios
	serializer_class = UserSerializer
	def get_queryset(self):
		return User.objects.all()

class UserSearchApiView(ListAPIView):# regresa un usuario por ID
	
	serializer_class = UserSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return User.objects.filter(
			id__icontains = id
		)


