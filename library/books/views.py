# views.py
from django.shortcuts import render , redirect
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .forms import BookForm , AuthorForm 


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def index(request):
    return render(request, 'index.html')


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'books/book_edit.html', {'form': form})


# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookFormSpesificAuthor

def create_book(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        form = BookFormSpesificAuthor(request.POST, author=author)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Kendi yönlendirmenizi ekleyin
    else:
        form = BookFormSpesificAuthor(author=author)
    return render(request, 'books/book_edit.html', {'form': form})

def book_list(request):
    books = Book.objects.all()  # fetch all books
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(book_detail , pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'GET':
        book.delete()
        return redirect(book_list)  # Tüm kitapların listelendiği view'ı yönlendirin
    return redirect(book_list)  # Tüm kitapların listelendiği view'ı yönlendirin



def author_new(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'authors/author_edit.html', {'form': form})


def author_list(request):
    authors = Author.objects.all()  # fetch all authors
    return render(request, 'authors/author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'authors/author_detail.html', {'author': author})


# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author
from .forms import AuthorForm  # Author formunuzu içe aktarın

def edit_author(request, id):
    ("request : ", request)
    ("id : ", id)
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            ("form saved succesfuly")
            return redirect(author_detail , pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors/edit_author.html', {'form': form})

def delete_author(request, id):
    ("author deleted succesfuly0")
    ("req met : ",request.method)
    author = get_object_or_404(Author, id=id)
    if request.method == 'GET':
        ("author deleted succesfuly1")
        author.delete()        
        ("author deleted succesfuly2")
        return redirect(author_list)  # Tüm author'ların listelendiği view'ı yönlendirin
    return redirect(author_list) 
