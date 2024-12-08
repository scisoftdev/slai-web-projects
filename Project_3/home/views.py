
from django.shortcuts import render
from .models import HomePageContent

def homepage_view(request):
    content = HomePageContent.objects.first()  # Assuming one entry is used for simplicity
    return render(request, 'home/index.html', {'content': content})
    