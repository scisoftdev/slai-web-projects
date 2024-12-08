
from django.db import models

class HomePageContent(models.Model):
    heading = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.heading
