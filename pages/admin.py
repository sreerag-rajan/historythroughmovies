from django.contrib import admin

from .models import RecentTheme, RecentThemeMovies, NextTheme, NextThemeMovies
# Register your models here.

admin.site.register(RecentTheme),
admin.site.register(RecentThemeMovies),
admin.site.register(NextTheme),
admin.site.register(NextThemeMovies)
