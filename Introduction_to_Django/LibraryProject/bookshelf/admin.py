from django.contrib import admin
from .models import Book
# Register your models here.

admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)


from django.contrib.auth.models import User

# Creating a new user
user = User.object.create_user('Ariyo', 'ariyoaribass68@gmail.com','Bekky$jesus')

# Retrieving the user name
user = User.object.get(username = 'Ariyo')