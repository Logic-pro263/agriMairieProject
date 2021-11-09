from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mairie import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mairie/', include('mairie.urls')),
    path('agri-m/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)