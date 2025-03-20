from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register, profile, CustomLogoutView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
]
