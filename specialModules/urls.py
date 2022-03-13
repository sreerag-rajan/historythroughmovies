from django.urls import path
from .views import specialModules_view, individualModulesView

smurlpatterns = [
    path("", specialModules_view),
    path("<slug:slug>/", individualModulesView),
]