from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
        widgets = {'title': forms.Textarea(attrs={'cols': 10}), 'text': forms.Textarea(attrs={'cols': 80})}


# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = ['text']
#         labels = {'text': ''}
#         widgets = {'text': forms.Textarea(attrs={'cols': 80})}
