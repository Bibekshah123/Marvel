from django.urls import path
from .views import SuperheroListView, SuperheroDetailView, SuperheroCreateView, SuperheroUpdateView, SuperheroDeleteView

urlpatterns = [
    path('', SuperheroListView.as_view(), name="hero_list"),
    path('hero/<int:pk>/', SuperheroDetailView.as_view(), name="hero_detail"),
    path('hero/add/', SuperheroCreateView.as_view(), name="hero_add"),
    path('hero/<int:pk>/edit/', SuperheroUpdateView.as_view(), name="hero_edit"),
    path('hero/<int:pk>/delete/', SuperheroDeleteView.as_view(), name="hero_delete"),
]
