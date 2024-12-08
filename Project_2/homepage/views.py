
from django.shortcuts import render
from .models import HomePageContent

def home(request):
    content = HomePageContent.objects.first()
    return render(request, 'home.html', {'content': content})
