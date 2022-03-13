
from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
from .models import Movies, Country, Language, Theme, Category, MovieTheme

def movies_all(request):	
	query = request.GET
	#setting stage for filteration
	categoryfilter = []
	languagefilter = []

	#checking if any queries have been passed
	if bool(query):
		#sort query
		if("sort" in query.keys()):
			sort = query['sort'];
		else:
			sort = "title";
		
		#category query
		if("category" in query.keys()):
			categories =query["category"].split("_");
			for cat in categories:
				categoryfilter.append(cat)
		
		#language query
		if("language" in query.keys()):
			languages =query["language"].split("_");
			for lang in languages:
				languagefilter.append(lang)	 
	else:
		sort = "title"
	
	#incase category and language is not present
	categories = Category.objects.all().order_by("category")
	languages = Language.objects.all()
	if(len(categoryfilter)==0):		
		for cat in categories:
			categoryfilter.append(cat)

	if(len(languagefilter)==0):		
		for lang in languages:
			languagefilter.append(lang)
		
	
	if (sort == 'length'):
		queryset = Movies.objects.all().filter(category__in=categoryfilter).filter(language__in=languagefilter).distinct().exclude(length=None).order_by("length")
	else:
		queryset = Movies.objects.all().filter(category__in=categoryfilter).filter(language__in=languagefilter).distinct().order_by(sort)	

	#Pagination			
	paginator = Paginator(queryset,20)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		'all_movies' : page_obj,
		"categories": categories,
		"languages": languages		 
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
	queryset1 = MovieTheme.objects.all().filter(theme = themeObj.theme).order_by('movie')
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