
from django.db import models

class HomePageContent(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title if self.title else "No Title"
    