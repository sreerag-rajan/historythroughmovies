from django.db import models
from autoslug import AutoSlugField


class Language(models.Model):
    language = models.CharField(max_length=100, primary_key=True)
    slug = AutoSlugField(populate_from='language', null = True)

    class Meta:
        ordering = ['language']

    def __str__(self):
        return self.language



class Theme(models.Model):
    theme = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='theme',null = True)

    class Meta:
        ordering = ['theme']

    def __str__(self):
        return self.theme


class Category(models.Model):
    category = models.CharField(max_length=100, primary_key=True)
    slug = AutoSlugField(populate_from="category",null = True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category


class Director(models.Model):
    director = models.CharField(max_length=100, primary_key=True)
    slug = AutoSlugField(populate_from="director",null = True)

    class Meta:
        ordering = ['director']

    def __str__(self):
        return self.director


class Country(models.Model):
    country = models.CharField(max_length=100, primary_key=True)
    slug = AutoSlugField(populate_from="country",null = True)

    class Meta:
        ordering = ['country']

    def __str__(self):
        return self.country


class Movies(models.Model):

    title = models.CharField(max_length=100)
    poster = models.URLField(default="https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/500x735.png")
    year = models.IntegerField()
    director = models.ManyToManyField(Director)
    language = models.ManyToManyField(Language)
    category = models.ManyToManyField(Category)
    length = models.CharField(max_length=10, help_text='Use HH:MM:SS format')
    country = models.ManyToManyField(Country)
    description = models.TextField(blank=True) 
    slug = AutoSlugField(populate_from="title",null = True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class MovieTheme(models.Model):
    movie = models.ForeignKey('Movies', on_delete=models.DO_NOTHING)
    theme = models.ForeignKey("Theme", on_delete=models.DO_NOTHING)
    text = models.TextField();

    def __str__(self):
        return self.movie.title + "-" +self.theme.theme
        
