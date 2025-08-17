from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Superhero
from .forms import SuperheroForm

class SuperheroListView(ListView):
    model = Superhero
    template_name = "marvel/superhero_list.html"
    context_object_name = "heroes"

class SuperheroDetailView(DetailView):
    model = Superhero
    template_name = "marvel/superhero_detail.html"
    context_object_name = "hero"

class SuperheroCreateView(CreateView):
    model = Superhero
    form_class = SuperheroForm
    template_name = "marvel/superhero_form.html"
    success_url = reverse_lazy("hero_list")

class SuperheroUpdateView(UpdateView):
    model = Superhero
    form_class = SuperheroForm
    template_name = "marvel/superhero_form.html"
    success_url = reverse_lazy("hero_list")

class SuperheroDeleteView(DeleteView):
    model = Superhero
    template_name = "marvel/superhero_confirm_delete.html"
    success_url = reverse_lazy("hero_list")
