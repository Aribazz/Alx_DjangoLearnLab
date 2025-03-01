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









# # Query all books by a specific author
# def books_by_author(author_name):
#     author = Author.objects.filter(name=author_name).first()
#     if author:
#         return Book.objects.filter(author=author)
#     return []

# # List all books in a library
# def books_in_library(library_name):
#     library = Library.objects.filter(name=library_name).first()
#     if library:
#         return library.books.all()
#     return []

# # Retrieve the librarian for a library
# def librarian_for_library(library_name):
#     library = Library.objects.filter(name=library_name).first()
#     if library:
#         return Librarian.objects.filter(library=library).first()
#     return None

# # Example Usage
# if __name__ == "__main__":
#     print("Books by Author 'John Doe':", books_by_author("John Doe"))
#     print("Books in Library 'Central Library':", books_in_library("Central Library"))
#     print("Librarian for 'Central Library':", librarian_for_library("Central Library"))
