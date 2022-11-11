from django.urls import path
from . import views

urlpatterns = [
  path('<str:genre>', views.films, name='films'),
  path('', views.genres, name='genres')
]