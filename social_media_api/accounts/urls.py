from django.urls import path, include
from .views import RegisterView, LoginView, UserProfileView
from django.contrib import admin
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
]