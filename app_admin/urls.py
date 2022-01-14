from django.urls import path
from . import views

urlpatterns = [
    path('admin-m', views.dashbord, name='indexDashbord'),
    path('toutes-les-cooeperatives', views.listingCooeperative, name='toutes-les-cooeperatives'),
    path('toutes-les-femmes', views.listing_woman, name='toutes-les-femmes'),
    path('modifier/cooeperative/<int:pk>', views.update_cooeperative, name='modifier-cooeperative'),
    path('effacer/femme/<int:pk>', views.delete_woman, name='supprimer-femme'),
    path('modifier/femme/<int:pk>/', views.update_woman, name='modifier-femme'),
    path('blog/admin/', views.index_post, name='index_post'),
    path('blog/admin/redation', views.create_post, name='create_post'),
    path('export_excel/', views.export_excel_c, name='export-excel'),
]

htmx_urlpatterns = [
    path('add-cooperative', views.add_cooperative, name='add-cooperative'),
    path('supprimer-cooeperative/<int:pk>', views.delete_cooeperative, name='delete-cooperative'),
]

urlpatterns += htmx_urlpatterns