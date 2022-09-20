from platform import release
from django.db import models

# Create your models here.
class FilmWatch(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.DateField() # format YYYY-MM-DD
    review = models.TextField()