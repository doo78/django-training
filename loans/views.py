from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.urls import reverse

import random

from .models import Book
from .forms import BookForm 

# Create your views here.
def welcome(request):
    
    slogans = ["Libraries make shhh happen.", "Believe in your shelf.", "Need a good read? We’ve got you covered.", "Check us out. And maybe one of our books too.", "Get a better read on the world.", "Having fun isn't hard when you've got a library card."]
    
    context = {'slogan': slogans[random.randint(0, len(slogans)-1)]}
    return render(request, 'welcome.html', context)

def books(request):
    
    context = {'books': Book.objects.all()}
    
    return render(request, 'books.html', context)

def get_book(request, book_id):
    
    try:
        book = Book.objects.get(pk=book_id)
        
        context = {'book' : (f"You're requesting a book with book_id {book_id}. Author: {book.authors}, Title: {book.title}")}
        
        return render(request, 'book.html', context)

    except Book.DoesNotExist:
         raise Http404(f"Could not find book with primary key {book_id}") 
        
    
def createBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None, 'Book cannot be saved.')
            else:
                path = reverse('books')
                return HttpResponseRedirect(path)
    else:
        form = BookForm()
    
    return render(request, 'create_book.html', {'form' : form})


def updateBook(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        
        if request.method == "POST":
            form = BookForm(request.POST, instance=book)
            
            if form.is_valid():
                try:
                    form.save()
                except:
                    form.add_error(None, 'Book cannot be saved.')
                else:
                    path = reverse('books')
                    return HttpResponseRedirect(path)
        else:
            form = BookForm(instance=book)        
        
        return render(request, 'update_book.html', {'form' : form, 'book' : book})

    except Book.DoesNotExist:
         raise Http404(f"Could not find book with primary key {book_id}") 
     
     
def loadDeleteBook(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        return render(request, 'delete_book.html', {'book': book})
    
    except Book.DoesNotExist:
        raise Http404(f"Could not find book with primary key {book_id}")
     
def deleteBook(request, book_id):
    book = Book.objects.get(pk=book_id)
    print(f"Deleting book: {book.title}")
    
    if request.method == "POST":
        book.delete()
        print("Book deleted successfully.")
        return HttpResponseRedirect(reverse('books'))
    
    return HttpResponseRedirect(reverse('books'))
    
