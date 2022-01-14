from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class':'form-control is-valid'}))
    pwd = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control is-valid'}))


class registerForm(forms.Form):
    first_name = forms.CharField(label="Nom:")
    last_name = forms.CharField(label="Prenom:")
    username = forms.CharField(label="Nom d'utilisateur:")
    email = forms.EmailField(label="Adresse Email:")
    pwd = forms.CharField(label="Mot de passe:", widget=forms.PasswordInput())
    pwd2 = forms.CharField(label="Confirmation mot de passe:", widget=forms.PasswordInput())
    conditions = forms.BooleanField()