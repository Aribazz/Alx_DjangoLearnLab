from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """Test cases for Book API endpoints."""

    def setUp(self):
        """Set up test data before each test."""
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create an author and book for testing
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author
        )

        # Define API endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book.id}/"
        self.delete_url = f"/api/books/delete/{self.book.id}/"

    ##  Test 1: List Books (GET /books/)
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # At least one book should exist

    ##  Test 2: Retrieve Single Book (GET /books/{id}/)
    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    ##  Test 3: Create a Book (POST /books/create/)
    def test_create_book(self):
        self.client.force_authenticate(user=self.user)  # Authenticate user
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Now there should be two books

    ##  Test 4: Update a Book (PUT /books/update/{id}/)
    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        data = {"title": "Updated Harry Potter", "publication_year": 1998, "author": self.author.id}
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Harry Potter")

    ##  Test 5: Delete a Book (DELETE /books/delete/{id}/)
    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # No books should remain

    ##  Test 6: Unauthorized User Access (POST /books/create/)
    def test_create_book_unauthorized(self):
        data = {"title": "Unauthorized Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Should fail without authentication

    ##  Test 7: Filtering Books (GET /books/?author=1)
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + f"?author={self.author.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['author'], self.author.id)

    ##  Test 8: Searching Books (GET /books/?search=Harry)
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    ## Test 9: Ordering Books (GET /books/?ordering=publication_year)
    def test_order_books(self):
        response = self.client.get(self.list_url + "?ordering=-publication_year")  # Descending order
        self.assertEqual(response.status_code, status.HTTP_200_OK)
