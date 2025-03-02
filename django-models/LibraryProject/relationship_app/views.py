from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Books,Library


def list_books(request):
    books=Book.objects.all()
    return render(request, "relationship_app/list_books.html")

# Check if 'LibraryDetailView' exists
class LibraryDetailView(DetailView):
    model=Library
    template_name="relationship_app/library_details.html"
    context_object_name = "library"
   
