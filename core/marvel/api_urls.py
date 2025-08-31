from django.urls import path
from .api_view import SuperheroListCreateAPIView, SuperheroRetrieveUpdateDestroyAPIView, UserSignupView


urlpatterns = [
    path('<str:version>/heroes/', SuperheroListCreateAPIView.as_view(), name='api_hero_list'),
    path('heroes/<int:pk>/', SuperheroRetrieveUpdateDestroyAPIView.as_view(), name='api_hero_detail'),
    path('signup/', UserSignupView.as_view(), name='signup'),
]
