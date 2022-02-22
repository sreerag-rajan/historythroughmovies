from django.urls import path
from .views import otherResources_view

orurlpatterns = [
    path("", otherResources_view),
]