from autoslug import AutoSlugField
from django.db import models

# Create your models here.
class SpecialModules(models.Model):
    moduleName = models.CharField(max_length=100)
    shortDiscription = models.TextField(blank=True);
    body= models.TextField()
    slug = AutoSlugField(populate_from="moduleName")

    class Meta:
        ordering = ['moduleName']

    def __str__(self):
        return self.moduleName
