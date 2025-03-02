from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book Model (ForeignKey to Author)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Library Model (ManyToManyField to Book)
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# Librarian Model (OneToOneField to Library)
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ROLE_CHOICE = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    role =models.CharField(max_length=20, choices=ROLE_CHOICE)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


    class Meta:
        permissions = [
            ('can_add_book', 'can add book'),
            ('can_change_book', 'can change book'),
            ('can_delete_book', 'can delete book'),
        ]