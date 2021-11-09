from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *

# Create your views here.
def login_mairie(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
                return render(request, 'app_login/login.html', context={'form':form})
        else:
            return render(request, 'app_login/login.html', context={'form': form})
    else:
        form = loginForm()
        return render(request, 'app_login/login.html', context={'form':form})

def register_mairie(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            pwd2 = form.cleaned_data['pwd2']
            if pwd == pwd2:
                pass
            else:
                messages.error(request, "Mot de passe non identique")
            conditions = form.cleaned_data['conditions']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=pwd)
            if user is not None:
                messages.success(request, f"Un compte a bien été créer pour {username} connectez-vous pour continuer")
                return redirect('loginPage')
            else:
                messages.error(request, "Echec de la création de compte")
                return render(request, 'app_login/register.html', context={'form':form})

    form = registerForm()
    return render(request, 'app_login/register.html', context={'form': form})


def Profile(request):
    return render(request, 'app_login/profile.html')