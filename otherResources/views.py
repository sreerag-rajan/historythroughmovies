import imp
from django.shortcuts import render

from .models import GoogleEarthModules

# Create your views here.

def otherResources_view(request):
    return render(request, "otherResources/otherResources.html")


def googleEarthModules_view(request):
    modules = GoogleEarthModules.objects.all();

    return render(request, "otherResources/googleEarthModules.html", {"modules":modules})

