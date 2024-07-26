# forms.py
from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author']  #   ,,,  replace with your actual fields
        


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']  #   ,,,  replace with your actual fields