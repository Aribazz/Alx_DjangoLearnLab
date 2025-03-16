from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['publication_year', 'author__name']


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_update(self, serializer):
        return super().perform_update(serializer)
    

class BookListView(ListView):
    """Django Class-Based View to list all books."""
    model = Book

    def render_to_response(self, context, **response_kwargs):
        books = list(context['object_list'].values())  # Convert QuerySet to list of dicts
        return JsonResponse(books, safe=False)

class BookDetailView(DetailView):
    """Django Class-Based View to retrieve a single book by ID."""
    model = Book

    def render_to_response(self, context, **response_kwargs):
        book = context['object']
        return JsonResponse({
            "id": book.id,
            "title": book.title,
            "publication_year": book.publication_year,
            "author": book.author.name
        })

@method_decorator(csrf_exempt, name='dispatch')
class BookCreateView(CreateView):
    """Django Class-Based View to create a new book."""
    model = Book
    fields = ['title', 'publication_year', 'author']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data['title'],
            publication_year=data['publication_year'],
            author_id=data['author']
        )
        return JsonResponse({
            "id": book.id,
            "title": book.title,
            "publication_year": book.publication_year,
            "author": book.author.name
        }, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class BookUpdateView(UpdateView):
    """Django Class-Based View to update an existing book."""
    model = Book
    fields = ['title', 'publication_year', 'author']

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        data = json.loads(request.body)
        book.title = data.get('title', book.title)
        book.publication_year = data.get('publication_year', book.publication_year)
        book.author_id = data.get('author', book.author.id)
        book.save()
        return JsonResponse({
            "id": book.id,
            "title": book.title,
            "publication_year": book.publication_year,
            "author": book.author.name
        })

@method_decorator(csrf_exempt, name='dispatch')
class BookDeleteView(DeleteView):
    """Django Class-Based View to delete a book."""
    model = Book

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()
        return JsonResponse({"message": "Book deleted"}, status=204)