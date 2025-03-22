from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register, profile, CustomLogoutView, edit_profile, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("edit-profile/", edit_profile, name="edit_profile"),
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("posts/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete", CommentDeleteView.as_view(), name="comment-delete"),
]
