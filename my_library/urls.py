"""
URL configuration for my_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from loans import views

urlpatterns = [
    #path('', views.welcome, name='home'),
    path('welcome/', views.welcome, name="welcome"),
    path('books/', views.books, name="books"),
    path('admin/', admin.site.urls),
    path('book/<int:book_id>', views.get_book, name="get_book"),
    path('create_book', views.createBook, name="create_book"),
    path('update_book/<int:book_id>', views.updateBook, name="update_book"),
    path('load_delete_book/<int:book_id>', views.loadDeleteBook, name="load_delete_book"),
    path('delete_book/<int:book_id>', views.deleteBook, name="delete_book"),


]
