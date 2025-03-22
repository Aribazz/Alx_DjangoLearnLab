from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment

# Create your tests here.
class CommentTests(TestCase):

    def setUp(self):
        """Set up test users, post, and comments."""
        self.user_a = User.objects.create_user(username="userA", password="testpass123")
        self.user_b = User.objects.create_user(username="userB", password="testpass123")
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user_a)
        self.comment = Comment.objects.create(post=self.post, author=self.user_a, content="Test Comment")

    # ✅ Test adding a comment (Authenticated User)
    def test_add_comment_authenticated(self):
        self.client.login(username="userA", password="testpass123")
        response = self.client.post(reverse("comment-create", kwargs={"post_id": self.post.id}), {"content": "New Comment"})
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertEqual(Comment.objects.count(), 2)  # A second comment should exist

    # ❌ Test adding a comment (Unauthenticated User)
    def test_add_comment_unauthenticated(self):
        response = self.client.post(reverse("comment-create", kwargs={"post_id": self.post.id}), {"content": "New Comment"})
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    # ✅ Test editing a comment (Author Only)
    def test_edit_comment_authorized(self):
        self.client.login(username="userA", password="testpass123")
        response = self.client.post(reverse("comment-update", kwargs={"post_id": self.post.id, "comment_id": self.comment.id}), {"content": "Updated Comment"})
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, "Updated Comment")

    # ❌ Test editing a comment (Unauthorized User)
    def test_edit_comment_unauthorized(self):
        self.client.login(username="userB", password="testpass123")
        response = self.client.post(reverse("comment-update", kwargs={"post_id": self.post.id, "comment_id": self.comment.id}), {"content": "Hacked Comment"})
        self.assertEqual(response.status_code, 403)  # Should be forbidden

    # ✅ Test deleting a comment (Author Only)
    def test_delete_comment_authorized(self):
        self.client.login(username="userA", password="testpass123")
        response = self.client.post(reverse("comment-delete", kwargs={"post_id": self.post.id, "comment_id": self.comment.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 0)  # Comment should be deleted

    # ❌ Test deleting a comment (Unauthorized User)
    def test_delete_comment_unauthorized(self):
        self.client.login(username="userB", password="testpass123")
        response = self.client.post(reverse("comment-delete", kwargs={"post_id": self.post.id, "comment_id": self.comment.id}))
        self.assertEqual(response.status_code, 403)  # Should be forbidden



