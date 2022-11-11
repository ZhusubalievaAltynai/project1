from django.shortcuts import render
from . import models

def films(request, genre):
  films = models.Films.objects.all()
  new_films = []
  for i in films:
    if i.genre == genre:
      new_films.append(i)
  return render(request, 'films.html', {'films': new_films})

def genres(request):
  return render(request, 'genres.html')