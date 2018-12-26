from django.shortcuts import render
from django.http import HttpResponse
from practica.models import Pelicula, Director, Usuario
from django.db.models.query import QuerySet

categorias = [("UK","unknown"),("AC","Action"),("AD","Adventure"),("AN","Animation"),("CH","Children's"),("CO","Comedy"),("CR","Crime"),
                          ("DO","Documentar"),("DR","Drama"),("FA","Fantasy"),("FN","Film-Noir"),("HR","Horror"),("MS","Musical"),
                          ("MY","Mystery"),("RO","Romance"),("SF","Sci-Fi"),
                          ("TH","Thriller"),("W","War"),("WS","Western")]
def index(request):
    return HttpResponse("Hello, world. You're at the practica index.")


def list_users(request):
    usuarios = Usuario.objects.all()
    return render(request, "list_user.html",{"usuarios":usuarios})
7

def list_peliculas(request):
    categories = [("UK", "unknown"), ("AC", "Action"), ("AD", "Adventure"), ("AN", "Animation"), ("CH", "Children's"),
                  ("CO", "Comedy"), ("CR", "Crime"),
                  ("DO", "Documentar"), ("DR", "Drama"), ("FA", "Fantasy"), ("FN", "Film-Noir"), ("HR", "Horror"),
                  ("MS", "Musical"),
                  ("MY", "Mystery"), ("RO", "Romance"), ("SF", "Sci-Fi"),
                  ("TH", "Thriller"), ("W", "War"), ("WS", "Western")]
    peliculas = {}
    for category in categories:
        peliculas[category[1]] = Pelicula.objects.filter(categoria=category[0])
    return render(request, "list_peliculas.html",{"peliculas":peliculas})

def list_directors(request):
    directores = Director.objects.all()
    peliculas = []
    for director in directores:
        director.pelicula_set.all()
        peliculas.append(Pelicula.objects.get(director_id=director.id))
    return render(request, "list_director.html",{"peliculas":peliculas, "directores":directores})