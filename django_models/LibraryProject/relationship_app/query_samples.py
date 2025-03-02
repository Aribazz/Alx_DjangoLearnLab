from .models import Author, Book, Library, Librarian


# Library.objects.get(name=library_name)

# Query all books by a specific author.
author_name = Author.objects.create(name="Ariyo")
author_name.save()
author= Author.objects.get(name=author_name)
author= Author.objects.filter(author=author)

# List all books in a library.
liberay_name = "Example_library_name"
books = Library.objects.get(name=liberay_name)
books.all()
# Retrieve the librarian for a library.
librarian_name = "Example_librarian_name"
librarian = Librarian.objects.get(library=liberay_name)








