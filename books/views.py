from django.shortcuts import get_object_or_404, render,redirect
from multiselectfield import MultiSelectField
from .models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author =request.POST['author']
        genre = request.POST['genre']
        language =request.POST['language']

        book= Book(book_name=book_name, author=author,genre=genre,language=language )
        book.save()
    
    return render(request,'home.html')

def show(request):
    books = Book.objects.all()
    data = {
        'books':books,
    }
    return render(request,'display.html',data)



def display(request,id):
    disp = get_object_or_404(Book,pk=id)
    data={
        'disp':disp,
    }
    return render(request,'details.html',data)

def search(request):
    books = Book.objects.all()
    genre_search = Book.objects.values_list('genre',flat=True).distinct()
    language_search = Book.objects.values_list('language',flat=True).distinct()
    author_search = Book.objects.values_list('author',flat=True).distinct()

    if 'genre' in request.GET:
        genre = request.GET['genre']
        if genre:
            books=books.filter(genre__iexact=genre)
    
    if 'language' in request.GET:
        language = request.GET['language']
        if language:
            books=books.filter(language__iexact=language)

    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            books=books.filter(author__iexact=author)


    data={
        'books':books,
        'genre_search':genre_search,
        'language_search':language_search,
        'author_search':author_search
    }
    return render(request,'search.html',data)
