from django.shortcuts import render
import csv
from django.http import HttpResponse
from movies.models import Movies


def printing_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="fulldatabase.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Title', 'Year', 'Director', 'language',
                     'Themes', 'Category', 'Lenght', 'Time Period', 'Country'])

    for movie in Movies.objects.all():
        writer.writerow([movie.title, movie.year, movie.director.all().values_list('director', flat=True), movie.language.all().values_list('language', flat=True),
                         movie.theme.all().values_list('theme', flat=True), movie.category.all().values_list('category', flat=True), movie.lenght, movie.time_period.all().values_list('time_period', flat=True), movie.country.all().values_list('country', flat=True)])

    return response
