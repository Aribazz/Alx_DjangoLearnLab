from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomerUser(AbstractUser):
    bio = models.TextField(max_length=200)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following")

    def __str__(self):
        return self.username