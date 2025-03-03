from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import Group

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "can view"),
            ("can_create", "can create"),
            ("can_edit", "can edit"),
            ("can_delete", "can delete"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class CustomUser(AbstractUser):
    date_of_birth =models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to="profile_photo/", blank=True, null=True)

    def __self__(self):
        return self.username


class CustomUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None, date_of_birth=None, profile_photo=None):
        pass
    def create_superuser(self, password=None, date_of_birth=None, profile_photo=None):
        pass

class UserGroup(Group):
    pass

    def __str__(self):
        return self.name