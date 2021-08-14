from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['language']

    def __str__(self):
        return self.language


class TimePeriod(models.Model):
    time_period = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.time_period


class Theme(models.Model):
    theme = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['theme']

    def __str__(self):
        return self.theme


class Category(models.Model):
    category = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category


class Director(models.Model):
    director = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['director']

    def __str__(self):
        return self.director


class Country(models.Model):
    country = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['country']

    def __str__(self):
        return self.country


class Movies(models.Model):

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.ManyToManyField(Director)
    language = models.ManyToManyField(Language)
    theme = models.ManyToManyField(Theme)
    category = models.ManyToManyField(Category)
    lenght = models.CharField(max_length=10, help_text='Use HH:MM:SS format')
    time_period = models.ManyToManyField(
        TimePeriod, help_text='If choosing Transitioning also choose from which period to which period')
    country = models.ManyToManyField(Country)
    para1 = models.TextField(blank=True)
    para2 = models.TextField(blank=True)
    para3 = models.TextField(blank=True)
    para4 = models.TextField(blank=True)
    para5 = models.TextField(blank=True)

    poster = models.ImageField(
        upload_to='posters/', blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
