from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
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
                return render(request, 'app_login/login.html', context={'form': form})
        else:
            return render(request, 'app_login/login.html', context={'form': form})
    else:
        form = loginForm()
        return render(request, 'app_login/login.html', context={'form': form})


def register_mairie(request):
    firstname = ''
    lastname = ''
    emailvalue = ''
    uservalue = ''
    passwordvalue1 = ''
    passwordvalue2 = ''


    form = registerForm(request.POST or None)

    if form.is_valid():

        firstname = form.cleaned_data.get('first_name')
        lastname = form.cleaned_data.get('last_name')
        emailvalue = form.cleaned_data.get('email')
        uservalue = form.cleaned_data.get('username')
        passwordvalue1 = form.cleaned_data.get('pwd')
        passwordvalue2 = form.cleaned_data.get('pwd2')
        if passwordvalue1 == passwordvalue2:
            try:
                user = User.objects.get(username=uservalue)
                c_email = User.objects.get(email=emailvalue)
                context = {'form': form, 'error1': "Choisir un autre nom d'utilisateur", 'error2': 'Choisir un autre adresse email'}
                return render(request, 'app_login/register.html', context)
            except User.DoesNotExist:
                user = User.objects.create_user(username=uservalue, password=passwordvalue1, email=emailvalue)

                fs = form.save()
                context = {'form': form}
                return render(request, 'app_login/login.html', context)
        else:
            context = {'form': form, 'error': 'Mot de passe non identique'}
            return render(request, 'app_login/register.html', context)

    else:
        context = {'form': form}
        return render(request, 'app_login/register.html', context)


def check_email(request):
    email = request.POST.get('email')
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse("<div id='email-error' class='error'>Adresse email non disponible </div>")
    else:
        return HttpResponse("<div id='email-error' class='success'>Adresse email  disponible </div>")


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>Nom d'utilisateur non disponible</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>Nom d'utilisateur disponible</div>")


def Profile(request):
    return render(request, 'app_login/profile.html')
