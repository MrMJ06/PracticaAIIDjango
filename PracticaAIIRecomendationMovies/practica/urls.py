from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('recomendacion/<int:u>', views.recomienda_peliculas_usuario),
path('recomendacion-pelicula/<int:u>', views.recomienda_peliculas_similares),
]