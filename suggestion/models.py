from django.db import models


# Create your models here.
class Suggestion(models.Model):
	title       = models.CharField(max_length = 100,)
	year        = models.IntegerField(blank = True, null = True)
	director    = models.CharField(max_length = 100, blank = True, null = True)
	language    = models.CharField(max_length = 100, blank = True, null = True)
	theme       = models.CharField(max_length = 100, blank = True, null = True)
	category    = models.CharField(max_length = 100, blank = True, null = True)
	lenght      = models.CharField(max_length = 10, blank = True, null = True)
	time_period = models.CharField(max_length = 100, blank = True, null = True)
	country     = models.CharField(max_length = 100, blank = True, null = True)

	def __str__(self):
		return self.title