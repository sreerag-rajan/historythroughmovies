from django import forms
from .models import Suggestion

class Suggestionform(forms.ModelForm):
	class Meta:
		model = Suggestion
		fields = [
			'title',
			'year',
			'director',
			'language',
			'theme',
			'category',
			'lenght',
			'time_period',
			'country'

		]