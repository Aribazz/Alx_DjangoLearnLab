from django.db import models

# Create your models here.
class Book(models.Model):
    title =models.CharFied(max_length=255)
    author=models.CharFied(max_length=255)

    def__str__(self):
        return self.title