
from django.shortcuts import render
from django.http import QueryDict
from .models import RecentTheme, RecentThemeMovies, NextTheme, NextThemeMovies

# Create your views here.
def home_view (request, *args, **kwrgs):
	recentTheme = RecentTheme.objects.all()
	recentThemePosters = RecentThemeMovies.objects.all()
	nextTheme = NextTheme.objects.all()
	nextThemeMovies = NextThemeMovies.objects.all()

	content = {
		"recentTheme": recentTheme,
		"nextTheme": nextTheme,
		"nextThemeMovies": nextThemeMovies,
		"recentThemePosters":recentThemePosters
		# "posters":posters
	}
	# print(content)
	
	return render(request, "index.html", content);


def about_view(request, *args, **kwrgs):
	return render(request, 'about.html')


def country_view(request, *args, **kwrgs):
	return render(request, 'countryselect.html')