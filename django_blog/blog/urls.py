from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register, profile, CustomLogoutView, edit_profile, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView, TagPostListView
from .views import SearchResultsView, PostByTagListView
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
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
    path("tags/<slug:tag_slug>/", TagPostListView.as_view(), name="tag-posts"),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="tag-posts"),
    path("search/", SearchResultsView.as_view(), name="search-results"),
]
