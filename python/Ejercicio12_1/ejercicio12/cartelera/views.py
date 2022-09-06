from django.shortcuts import render
from .models import Author, Film

# Create your views here.
def index(request):
    num_films = Film.objects.all().count
    num_authors = Author.objects.all().count

    return render(
        request,
        'index.html',
        context={
            'num_films': num_films,
            'num_authors': num_authors
        }
    )