from django.db import models

# Create your models here.
class GoogleEarthModules(models.Model):
    moduleName= models.CharField(max_length=100)
    shortDescription= models.TextField()
    url = models.URLField()

    class Meta:
        ordering = ['moduleName']

    def __str__(self):
        return self.moduleName