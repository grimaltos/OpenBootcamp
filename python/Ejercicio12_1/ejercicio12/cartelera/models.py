from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=64, help_text='Nombre del autor')

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=64, help_text='Nombre de la pelicula')
    autor = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    anyo = models.IntegerField(max_length=4, help_text='Año de lanzamiento')

    def __str__(self):
        return self.title