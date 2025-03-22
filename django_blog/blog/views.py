from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BlogPost
from .forms import BlogPostForm
from .models import Post, Commit
from .forms import CommentForm


# Create your views here.


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Custom Registration View
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

# Profile View (Only for Logged-in Users)
@login_required
def profile(request):
    return render(request, "blog/profile.html")


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, "blog/edit_profile.html", {"form": form})


# Logout User
class CustomLogoutView(LogoutView):
    next_page = "login" 



# List all blog posts
class PostListView(ListView):
    model = BlogPost
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

# Show details of a single post
class PostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"
    form_class = BlogPostForm

# Create a new blog post (only for logged-in users)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    form_class = BlogPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update an existing post (only for the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    form_class = BlogPostForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete a post (only for the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Commit
    form_class = CommentForm
    template_name = "blog/post_detail.html"  # Uses the post detail template

    def form_valid(self, form):
        """Assign the comment to the logged-in user and associated post."""
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect back to the post after commenting."""
        return self.object.post.get_absolute_url()


# View to edit a comment (Only the author can edit)
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Commit
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def test_func(self):
        """Ensure only the comment's author can edit."""
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """Redirect back to the post after updating."""
        return self.object.post.get_absolute_url()

# View to delete a comment (Only the author can delete)
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Commit
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        """Ensure only the comment's author can delete."""
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """Redirect back to the post after deleting."""
        return self.object.post.get_absolute_url()