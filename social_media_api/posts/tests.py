from django.test import TestCase
# from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")  # Authenticate user
        self.post = Post.objects.create(author=self.user, title="Test Post", content="Test Content")

    def test_get_posts(self):
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_authenticated(self):
        data = {"title": "New Post", "content": "Some content"}
        response = self.client.post("/api/posts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_unauthenticated(self):
        self.client.logout()
        data = {"title": "New Post", "content": "Some content"}
        response = self.client.post("/api/posts/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_post_by_owner(self):
        data = {"title": "Updated Title"}
        response = self.client.patch(f"/api/posts/{self.post.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post_by_other_user(self):
        other_user = User.objects.create_user(username="otheruser", password="testpass")
        self.client.force_authenticate(user=other_user)
        data = {"title": "Updated Title"}
        response = self.client.patch(f"/api/posts/{self.post.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_post_by_owner(self):
        response = self.client.delete(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_post_by_other_user(self):
        other_user = User.objects.create_user(username="otheruser", password="testpass")
        self.client.force_authenticate(user=other_user)
        response = self.client.delete(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FeedTests(APITestCase):

    def setUp(self):
        """Set up users and posts"""
        self.user1 = User.objects.create_user(username="user1", password="pass123")
        self.user2 = User.objects.create_user(username="user2", password="pass123")
        self.client.login(username="user1", password="pass123")

        self.post = Post.objects.create(author=self.user2, content="Test post")

    def test_feed_without_following(self):
        """Check feed when user is not following anyone"""
        response = self.client.get('/posts/feed/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_feed_with_following(self):
        """Check feed when user follows another user"""
        self.user1.following.add(self.user2)
        response = self.client.get('/posts/feed/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)