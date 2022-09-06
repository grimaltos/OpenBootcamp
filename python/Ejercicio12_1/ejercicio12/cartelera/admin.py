from django.contrib import admin

# Register your models here.

from .models import Author, Film

admin.site.register(Author)
admin.site.register(Film)