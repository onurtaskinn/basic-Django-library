# Create your models here.

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def books(self):
        return Book.objects.filter(author=self)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name    