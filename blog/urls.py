from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList, name='indexBlog'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
]
