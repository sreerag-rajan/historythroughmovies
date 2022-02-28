from django.db import models

# Create your models here.
class RecentTheme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RecentThemeMovies(models.Model):
    movieName = models.CharField(max_length=100)
    posterUrl = models.URLField()

    def __str__(self):
        return self.movieName


class NextTheme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NextThemeMovies(models.Model):
    movieName = models.CharField(max_length=100)

    class Meta:
        ordering = ['movieName']

    def __str__(self):
        return self.movieName

    