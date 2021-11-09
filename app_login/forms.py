from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class':'form-control is-valid'}))
    pwd = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control is-valid'}))


class registerForm(forms.Form):
    first_name = forms.CharField(label="Nom:", widget=forms.TextInput(attrs={'class': 'form-control is-valid'}))
    last_name = forms.CharField(label="Prenom:", widget=forms.TextInput(attrs={'class': 'form-control is-valid'}))
    username = forms.CharField(label="Nom d'utilisateur:", widget=forms.TextInput(attrs={'class': 'form-control is-valid'}))
    email = forms.EmailField(label="Adresse Email:", widget=forms.TextInput(attrs={'class': 'form-control is-valid'}))
    pwd = forms.CharField(label="Mot de passe:", widget=forms.PasswordInput(attrs={'class': 'form-control is-valid'}))
    pwd2 = forms.CharField(label="Confirmation mot de passe:", widget=forms.PasswordInput(attrs={'class': 'form-control is-valid'}))
    conditions = forms.BooleanField()