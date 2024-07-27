# forms.py
from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author']  #   ,,,  replace with your actual fields


class BookFormSpesificAuthor(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)  # Author'ı kwargs'dan alın
        super(BookFormSpesificAuthor, self).__init__(*args, **kwargs)
        if 'author' in self.fields:
            del self.fields['author']  # Formdan author alanını kaldır

    def save(self, commit=True):
        instance = super(BookFormSpesificAuthor, self).save(commit=False)
        if self.author:
            instance.author = self.author  # Author'ı instance'a ata
        if commit:
            instance.save()
        return instance


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']  #   ,,,  replace with your actual fields