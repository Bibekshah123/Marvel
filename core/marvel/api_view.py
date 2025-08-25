from rest_framework import generics, permissions
from .models import Superhero
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]

# List + Create (GET all, POST new)
class SuperheroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Superhero.objects.all()
    serializer_class = SuperheroSerializer
    permission_classes = [IsAuthenticated]

# Retrieve + Update + Delete (GET one, PUT/PATCH, DELETE)
class SuperheroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Superhero.objects.all()
    serializer_class = SuperheroSerializer
    permission_classes = [IsAuthenticated]
