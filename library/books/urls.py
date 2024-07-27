# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (AuthorViewSet, BookViewSet, index, 
                    book_new,book_list, book_detail, edit_book, delete_book, create_book,
                    author_new, author_list , author_detail, edit_author , delete_author,
                    )

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),

    path('book/new/', book_new, name='book_new'),
    path('books/', book_list, name='book_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('book/<int:id>/edit/', edit_book, name='edit_book'),
    path('book/<int:id>/delete/', delete_book, name='delete_book'),    
    path('book/add/<int:author_id>', create_book, name='create_book'),

    path('author/new/', author_new, name='author_new'),
    path('authors/', author_list, name='author_list'),
    path('author/<int:pk>/', author_detail, name='author_detail'),
    path('author/<int:id>/edit/', edit_author, name='edit_author'),
    path('author/<int:id>/delete/', delete_author, name='delete_author'),
]



