from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Suggestionform


# Create your views here.
# def suggest_movies(request):
# 	return render(request, 'suggestion.html')
from .forms import Suggestionform

def suggestion_create_view(request):
    form = Suggestionform(request.POST or None)
    # if this is a POST request we need to process the form data
    
    # check whether it's valid:
    if form.is_valid():
        
        form.save()
        form = Suggestionform()

    else:
        form = Suggestionform()

    return render(request, 'suggestion.html', {'form': form})