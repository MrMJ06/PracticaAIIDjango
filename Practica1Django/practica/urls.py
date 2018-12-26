from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.list_users),
    path('films/', views.list_peliculas),
    path('directors/', views.list_directors),
]