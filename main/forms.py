from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags"]

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),  # Allow users to select from all categories
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for multiple selection
        required=False  # Make the field optional
    )