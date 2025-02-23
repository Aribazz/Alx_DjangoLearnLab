import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return Book.objects.filter(author=author)
    return None

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.books.all()
    return None

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.librarian
    return None
