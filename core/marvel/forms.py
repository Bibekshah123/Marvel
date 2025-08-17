from django import forms
from .models import Superhero

class SuperheroForm(forms.ModelForm):
    class Meta:
        model = Superhero
        fields = ['name', 'power', 'description', 'image']
