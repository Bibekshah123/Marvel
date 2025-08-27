from rest_framework import generics, permissions
from .models import Superhero
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User


class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]
    
# 🔹 Custom Login API (JWT based)
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if not user:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT token manually
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

# List + Create (GET all, POST new)
class SuperheroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Superhero.objects.all()
    serializer_class = SuperheroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Retrieve + Update + Delete (GET one, PUT/PATCH, DELETE)
class SuperheroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Superhero.objects.all()
    serializer_class = SuperheroSerializer
    permission_classes = [IsAuthenticated]
