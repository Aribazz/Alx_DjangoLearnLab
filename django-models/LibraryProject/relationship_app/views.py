from django.shortcuts import render
from django.views.generic.detail import DetailView,CreateView
from .models import Books
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.url import reverse_lazy
from django.contrib.auth import login


def list_books(request):
    books=Book.objects.all()
    return render(request, "relationship_app/list_books.html")

# Check if 'LibraryDetailView' exists
class LibraryDetailView(DetailView):
    model=Library
    template_name="relationship_app/library_detail.html"
    context_object_name = "library"
   
class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"
