from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    path('books/list', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)),
]