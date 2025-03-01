from django.shortcuts import render
from django.views import View  # If you're using class-based views

# ✅ Check if 'list_books' is defined
def list_books(request):
    return render(request, "books_list.html")

# ✅ Check if 'LibraryDetailView' exists
class LibraryDetailView(View):
    def get(self, request):
        return render(request, "library_detail.html")
