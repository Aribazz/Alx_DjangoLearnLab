from django import forms
from .models import BlogPost
from .models import Commit


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter post title"}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your content here", "rows": 5}),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
    

class CommentForm(forms.ModelForm):
    """Form for adding and editing comments."""
    
    class Meta:
        model = Commit
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your comment...", "rows": 3}),
        }

    def clean_content(self):
        """Ensure the comment is not empty."""
        content = self.cleaned_data.get("content")
        if not content.strip():
            raise forms.ValidationError("Comment cannot be empty.")
        return content

