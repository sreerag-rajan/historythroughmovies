from django.shortcuts import render

from .models import SpecialModules
# Create your views here.

def specialModules_view(request):
    modules = SpecialModules.objects.all()

    content = {
        "modules": modules
    }

    return render(request, "specialModules\specialModules.html",content)


def individualModulesView(request,slug):
    module = SpecialModules.objects.get(slug=slug)

    content = {
        "module":module
    }

    return render(request,"specialModules\individualSPModule.html",content)