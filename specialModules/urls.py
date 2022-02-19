from django.urls import path
from .views import specialModules_view

smurlpatterns = [
    path("", specialModules_view),
]