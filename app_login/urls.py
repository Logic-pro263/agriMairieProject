from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('connexion', views.login_mairie, name='loginPage'),
    path('inscription', views.register_mairie, name='registerPage'),
    path('deconnexion', LogoutView.as_view(next_page='loginPage'), name='logoutPage'),
    path('profil', views.Profile, name='profilePage'),
]