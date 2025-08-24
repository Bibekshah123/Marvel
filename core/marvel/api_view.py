from rest_framework import generics, permissions
from .models import Superhero
from .serializers import SuperheroSerializer
from rest_framework.permissions import IsAuthenticated




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
