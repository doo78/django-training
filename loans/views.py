from django.shortcuts import render

import random

from .models import Book

# Create your views here.
def welcome(request):
    
    slogans = ["Libraries make shhh happen.", "Believe in your shelf.", "Need a good read? We’ve got you covered.", "Check us out. And maybe one of our books too.", "Get a better read on the world.", "Having fun isn't hard when you've got a library card."]
    
    context = {'slogan': slogans[random.randint(0, len(slogans)-1)]}
    return render(request, 'welcome.html', context)

def books(request):
    
    context = {'books': Book.objects.all()}
    
    return render(request, 'books.html', context)
