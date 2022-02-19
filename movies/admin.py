from django.contrib import admin

# Register your models here.
from .models import Language, Theme, Category, Country, Movies, Director,MovieTheme
admin.site.register(Language),
admin.site.register(Theme),
admin.site.register(Category),
admin.site.register(Director),
admin.site.register(Country),

admin.site.register(Movies)
admin.site.register(MovieTheme)
