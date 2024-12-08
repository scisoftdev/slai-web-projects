from django.shortcuts import render
from .models import HomePageContent

def home(request):
    content = HomePageContent.objects.first()
    if content:
        return render(request, 'slai/home.html', {'content': content})
    else:
        return render(request, 'slai/home.html', {'error': 'Контент не найден'})