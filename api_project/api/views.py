from rest_framework import generics
from .models import Book
from .serializersa import BookSerializer


# Create your views here.
class BookList(generics.BookSerializer):
    queryset = Book.object.all()
    serializer_class = BookSerializer
