from django.urls import path
from .views import otherResources_view, googleEarthModules_view

orurlpatterns = [
    path("", otherResources_view),
    path("googleEarthModules", googleEarthModules_view),
]