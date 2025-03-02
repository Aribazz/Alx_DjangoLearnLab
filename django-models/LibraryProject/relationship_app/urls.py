from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView,LogoutView,
from .views import SignUpView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name="login.html"),name="login"),
    path('logout/', LogoutView.as_view(template_name="logout.html"),name="logout"),
    path('signup/', SignUpView.as_view(template_name="register.html"),name="signup"),
    path('register/', views.register, name='register'),
]
