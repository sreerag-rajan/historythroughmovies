from django.shortcuts import render

# Create your views here.
from .models import Movies, Country, Language, Theme, Category, MovieTheme

def movies_all(request, sort= 'title'):	
	queryset = Movies.objects.all().order_by(sort)
	context = {
		'all_movies' : queryset,		 
	}
	return render(request, "all_movies.html", context)


def movies_countries(request, country):
	queryset = Movies.objects.all().filter(country =country).order_by('title')
	context = {
		'movies_country': queryset,
		'Country': country,
		
	}
	return render (request, 'movies_country.html', context)



def themes_all(request):
	queryset = Theme.objects.all().order_by('theme')
	context = {
		'allthemes' : queryset,
			 
	}
	return render(request, "allthemes.html", context)


def themes_view_individual(request, theme):
	queryset1 = MovieTheme.objects.all().filter(theme = theme).order_by('theme')
	queryset2 = Theme.objects.get(slug = theme)
	context = {
		'eachtheme': queryset2,
		'Movies': queryset1,
		'Theme': theme,
		
	}
	return render (request, 'eachtheme.html', context)

def movie_detail(request, movie):
	queryset= Movies.objects.get(slug=movie)
	context ={
		'Movie' : queryset
	}

	return render(request, 'movie.html', context)