from django import forms
from .model import Book, CustomUser

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo']

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            return redirect('success_url')  # Replace 'success_url' with your success URL
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})