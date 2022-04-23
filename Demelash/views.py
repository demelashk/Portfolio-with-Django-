from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

# Home
home = Home.objects.latest('updated')

context = {
        'home': home,

    }

def index(request):
    return render(request, 'index.html', context)
