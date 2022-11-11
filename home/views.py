from django.shortcuts import render

def home(request):
  genres=(
    'horror',
    'romantic',
    'fantasy',
    'comedy'
  )
  return render(request, 'home.html')