from django.urls import path
from .views import AuthorListCreateView, BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/list/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail')
]
