from django.db import models

class HomePageContent(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title