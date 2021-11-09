from django.urls import path
from . import views

urlpatterns = [
    path('admin-m', views.dashbord, name='indexDashbord'),
    path('toutes-les-cooeperatives', views.listingCooeperative, name='toutes-les-cooeperatives'),
    path('toutes-les-femmes',views.listing_woman, name='toutes-les-femmes'),
    path('modifier/cooeperative/<int:pk>', views.update_cooeperative, name='modifier-cooeperative'),
    path('supprimer/cooeperative/<int:pk>', views.delete_cooeperative, name='supprimer-cooeperative'),
    path('effacer/femme/<int:pk>', views.delete_woman, name='supprimer-femme'),
    path('modifier/femme/<int:pk>/', views.update_woman, name='modifier-femme'),
]