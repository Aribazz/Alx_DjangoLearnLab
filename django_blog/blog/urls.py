from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register, profile, CustomLogoutView, edit_profile

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("edit-profile/", edit_profile, name="edit_profile")
]
