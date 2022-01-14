from django import forms
from .models import Cooeperatives, Members, CooperativeComment, MemberComment
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class cooeperativeForm(forms.ModelForm):
    class Meta:
        model = Cooeperatives
        fields = ['name', 'name_president', 'creation_date', 'members_in', 'city', 'description', 'image']
        labels = {'name': 'Nom de la cooeperative', 'name_president': 'Nom de la presidente', 'creation_date': 'Date de Création', 'members_in': 'Nombre de membre', 'city': 'Village', 'description': 'Description', 'image': 'image'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la Coopérative'}),
            'name_president': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la présidente'}),
            'creation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'members_in': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Nombre de femme'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'village'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Description de '
                                                                                                    'la coopérative'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class membersForm(forms.ModelForm):
    phone_number: PhoneNumberField()
    class Meta:
        model = Members
        fields = ['name', 'born_date', 'city', 'phone_number', 'gender', 'activity', 'picture', 'cooeperative']
        labels = {'name': 'Nom', 'born_date': 'Date de naissance', 'city': 'Village', 'phone_number': 'Numéro de phone', 'gender': 'Sexe', 'activity': 'Activité', 'picture': 'Image','cooeperative': 'Cooéperative'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'born_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': PhoneNumberPrefixWidget(initial='ML', attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'activity': forms.Textarea(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'cooeperative': forms.Select(attrs={'class': 'form-control', }),
        }

class CooperativeCommentForm(forms.ModelForm):
    class Meta:
        model = CooperativeComment
        fields = ['full_name', 'Subject', 'email', 'comment']
        labels = {'full_name': 'Nom complet', 'Subject': 'Sujet', 'email': 'Email', 'comment': 'Commentaire'}
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'Subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre commentaire'}),
        }

class MemberCommentForm(forms.ModelForm):
    class Meta:
        model = MemberComment
        fields = ['full_name', 'Subject', 'email', 'comment']
        labels = {'full_name': 'Nom complet', 'Subject': 'Sujet', 'email': 'Email', 'comment': 'Commentaire'}
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'Subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre commentaire'}),
        }