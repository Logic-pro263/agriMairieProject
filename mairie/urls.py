from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='indexPage'),
    path('liste-des-cooeperatives', views.cooeperativeList, name='CooeperativePage'),
    path('liste-des-femmes', views.womanList, name='womanPage'),
    path('cooeperative/detail/<int:id_cooeperative>', views.detailCooperative, name='detailCooeperative'),
    path('femmes/detail/<int:id_member>', views.detailWoman, name='detailWoman'),
    path('resultat', views.search_r, name='resultat'),
    path('galerie', views.gallery, name='galleryPage'),
    path('a-propos-de', views.about, name='aboutPage'),
    path('contact', views.contact, name='contactPage'),
    path('mon-compte/', include('app_login.urls')),
    path('blog/', include('blog.urls')),
    path('adminmairie/', include('app_admin.urls')),
    path('localisation/', include('addresses.urls')),
]