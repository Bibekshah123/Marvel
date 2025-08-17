from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    power = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="superheroes/")

    def __str__(self):
        return self.name
