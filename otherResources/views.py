from django.shortcuts import render

# Create your views here.

def otherResources_view(request):
    return render(request, "otherResources/otherResources.html")
