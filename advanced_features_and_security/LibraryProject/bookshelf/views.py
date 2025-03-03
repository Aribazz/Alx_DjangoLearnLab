from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Books
from .forms import ExampleForm

# Create your views here.
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_list(request):
    all_books = Book.objects.all()
    response = render(request, "bookshelf/book_list.html", {"all_books":all_books})
    return response