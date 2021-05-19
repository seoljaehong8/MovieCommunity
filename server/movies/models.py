from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default=0)
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    vote_average = models.FloatField(default=0.0)
    vote_count = models.IntegerField(default=0)
    popularity = models.FloatField(default=0.0)

