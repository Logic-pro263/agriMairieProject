from django import forms
from blog.models import Post

class blogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'author', 'content', 'image', 'published'
        ]
        labels = {
            'title': 'Titre', 'author': 'Auteur', 'content': 'Article', 'image': 'Image', 'published': 'Publié',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Auteur'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenue'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'published': forms.RadioSelect(attrs={'class': 'form-control'}),
        }