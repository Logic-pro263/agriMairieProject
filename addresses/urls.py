from django.urls import path
from . import views

urlpatterns = [
    path('localisation', views.mapPage, name='mapPage'),
]