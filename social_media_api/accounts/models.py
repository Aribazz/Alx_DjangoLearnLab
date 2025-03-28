from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class CustomUser(AbstractUser):
    # bio = models.TextField(max_length=200)
    # profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    # followers = models.ManyToManyField("self", symmetrical=False, related_name="following")
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)
    
    def __str__(self):
        return self.username
    
    def follow(self, user):
        """Follow another user."""
        self.following.add(user)

    def unfollow(self, user):
        """Unfollow a user."""
        self.following.remove(user)

    def is_following(self, user):
        """Check if the user is following another user."""
        return self.following.filter(id=user.id).exists()
