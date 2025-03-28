from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class FollowUnfollowTests(APITestCase):

    def setUp(self):
        """Set up test users"""
        self.user1 = User.objects.create_user(username="user1", password="pass123")
        self.user2 = User.objects.create_user(username="user2", password="pass123")
        self.client.login(username="user1", password="pass123")

    def test_follow_user(self):
        """Test user1 following user2"""
        response = self.client.post(f'/accounts/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user2, self.user1.following.all())

    def test_unfollow_user(self):
        """Test user1 unfollowing user2"""
        self.user1.following.add(self.user2)
        response = self.client.post(f'/accounts/unfollow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn(self.user2, self.user1.following.all())

