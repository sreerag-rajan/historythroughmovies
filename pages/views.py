
from django.shortcuts import render

# Create your views here.
def home_view (request, *args, **kwrgs):
	return render(request, "index.html")


def about_view(request, *args, **kwrgs):
	return render(request, 'about.html')


def country_view(request, *args, **kwrgs):
	return render(request, 'countryselect.html')