
from django.shortcuts import render
from django.db import connection

# Create your views here.
from .models import Movies, Country, Language, Theme, Category, MovieTheme

def movies_all(request):	
	query = request.GET
	
	if bool(query):
		if("sort" in query.keys()):
			sort = query['sort'];
		else:
			sort = "title";
		if("category" in query.keys()):
			category = query['category'] 
	else:
		sort = "title"
	

	if (sort == 'length'):
		queryset = Movies.objects.all().exclude(length=None).order_by("length")
	else:
		queryset = Movies.objects.all().order_by(sort)
	context = {
		'all_movies' : queryset,		 
	}
	return render(request, "all_movies.html", context)


def movies_countries(request, country):
	query = request.GET
	
	if bool(query):
		if("sort" in query.keys()):
			sort = query['sort'];
		else:
			sort = "title";
		if("category" in query.keys()):
			category = query['category'] 
	else:
		sort = "title"
	queryset = Movies.objects.all().filter(country =country).order_by(sort)
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
	# queryset1 = MovieTheme.objects.all().filter(theme = theme).order_by('theme')

	themeObj = Theme.objects.get(slug = theme)
	queryset1 = MovieTheme.objects.all().filter(theme = themeObj.theme).order_by('theme')
	context = {
		'eachtheme': themeObj,
		'Movies': queryset1,		
	}
	return render (request, 'eachtheme.html', context)

def movie_detail(request, movie):
	queryset= Movies.objects.get(slug=movie)
	theme = MovieTheme.objects.all().filter(movie= queryset.id)
	context ={
		'Movie' : queryset,
		'Themes': theme
	}

	return render(request, 'movie.html', context)