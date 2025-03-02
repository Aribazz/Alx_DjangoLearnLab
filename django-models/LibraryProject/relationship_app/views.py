from django.shortcuts import render
from django.views.generic.detail import DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Books
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.url import reverse_lazy
from django.contrib.auth import login


def list_books(request):
    books=Book.objects.all()
    return render(request, "relationship_app/list_books.html")

# Check if 'LibraryDetailView' exists
class LibraryDetailView(DetailView):
    model=Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
   
class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

@user_passes_test(lambda u: u.userprofile.role == 'Admin')
class AdminView(TemplateView):
    template_name = "relationship_app/admin_view.html"

@user_passes_test(lambda u: u.userprofile.role == "Librarian")
class LibrarianView(TemplateView):
    template_name = "relationship_app/librarian_view.html"

@user_passes_test(lambda u: u.userprofile.role == "Member")
class MemberView(TemplateView):
    template_name = "relationship_app/member_view.html"


@method_decorator(permission_required("relationship_app.can_add_book", raise_exception=True), name ="can add book")
class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "published_date"]
    template_name = "relationship_app/book_form.html"
    sources_url = reverse_lazy('book_list')

@method_decorator(permission_required("relationship_app.can_change_book", raise_exception=True), name ="can change book")
class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "author", "published_date"]
    template_name = "relationship_app/book_form.html"
    sources_url = reverse_lazy('book_list')

@method_decorator(permission_required("relationship_app.can_delete_book", raise_exception=True), name ="can delete book")
class BookDeleteView(DeleteView):
    model = Book
    template_name = "relationship_app/book_form.html"
    sources_url = reverse_lazy('book_list')