"""historythroughmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from movies.models import Theme
from movies.views import movies_all, movies_countries, themes_all, themes_view_individual, movie_detail
from pages.views import home_view, about_view, country_view
from printingdata.views import printing_csv
from suggestion.views import suggestion_create_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('allmovies/', movies_all, name='all movies'),
    path('movies_set_in_<str:country>/', movies_countries),
    path('allmovies/<str:sort>/', movies_all),
    path('themes/', themes_all, name='Themes'),
    path('themes/theme_<str:theme>/', themes_view_individual),
    path('export', printing_csv),
    path('suggestion/', suggestion_create_view),
    path('movie-<str:movie>/', movie_detail),
    path('about/', about_view, name='about'),
    path('countries/', country_view),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from movies.views import movies_all, movies_countries
