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

def book_list(request):
    books = Book.objects.all()  # fetch all books
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})





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
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            print("form saved succesfuly")
            return redirect(author_detail , pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors/edit_author.html', {'form': form})

def delete_author(request, id):
    print("author deleted succesfuly0")
    print("req met : ",request.method)
    author = get_object_or_404(Author, id=id)
    if request.method == 'GET':
        print("author deleted succesfuly1")
        author.delete()        
        print("author deleted succesfuly2")
        return redirect(author_list)  # Tüm author'ların listelendiği view'ı yönlendirin
    return redirect(author_list) 
