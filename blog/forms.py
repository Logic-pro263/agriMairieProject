from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'subject', 'email', 'comment']
        labels = {'full_name': 'Nom complet', 'subject': 'Sujet', 'email': 'Email', 'comment': 'Commentaire'}
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre commentaire'}),
        }