from rest_framework.generics import ListAPIView
from .models import Book
from .serializersa import BookSerializer


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer
