from django.urls import path
from .api_view import SuperheroListCreateAPIView, SuperheroRetrieveUpdateDestroyAPIView, UserSignupView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('heroes/', SuperheroListCreateAPIView.as_view(), name='api_hero_list'),
    path('heroes/<int:pk>/', SuperheroRetrieveUpdateDestroyAPIView.as_view(), name='api_hero_detail'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),

    
    # Token Authentication
    # path('api/token-auth/', obtain_auth_token, name='api_token_auth'),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
