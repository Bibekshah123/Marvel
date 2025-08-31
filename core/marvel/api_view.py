from rest_framework import generics, permissions
from .models import Superhero
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from rest_framework.throttling import UserRateThrottle
from .pagination import *
from rest_framework.response import Response


class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [UserRateThrottle]

    

# List + Create (GET all, POST new)
class SuperheroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Superhero.objects.all()
    serializer_class = SuperheroSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    pagination_class = SuperheroPagination
    
    def list(self, request, *args, **kwargs):
        version = request.version  # get version from URL
        superheroes = self.get_queryset()
        serializer = self.get_serializer(superheroes, many=True)

        # Customize response based on version
        if version == 'v1':
            return Response({"superheroes": serializer.data})
        elif version == 'v2':
            return Response({
                "count": superheroes.count(),
                "results": serializer.data
            })

# Retrieve + Update + Delete (GET one, PUT/PATCH, DELETE)
class SuperheroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Superhero.objects.all()
    serializer_class = SuperheroSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

