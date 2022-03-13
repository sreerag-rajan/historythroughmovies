from django import forms
from .models import Suggestion

class Suggestionform(forms.ModelForm):
	class Meta:
		model = Suggestion
		fields = [
			'title',
			'year',
			'director',
			'theme',
			'category',			
			'country'
		]
