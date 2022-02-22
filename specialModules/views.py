from django.shortcuts import render

# Create your views here.

def specialModules_view(request):
    return render(request, "specialModules\specialModules.html",)
