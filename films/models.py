from django.db import models

class Films(models.Model):
  GENRES = (
    ('horror', 'horror'),
    ('romantic', 'romantic'),
    ('fantasy', 'fantasy'),
    ('comedy', 'comedy'),
  )
  title = models.CharField(max_length=100)
  price = models.IntegerField()
  genre = models.CharField(choices=GENRES, max_length=100)
  rating = models.PositiveIntegerField()