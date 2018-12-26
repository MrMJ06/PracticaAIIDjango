from django.db import models

categories = [("UK","unknown"),("AC","Action"),("AD","Adventure"),("AN","Animation"),("CH","Children's"),("CO","Comedy"),("CR","Crime"),
                          ("DO","Documentar"),("DR","Drama"),("FA","Fantasy"),("FN","Film-Noir"),("HR","Horror"),("MS","Musical"),
                          ("MY","Mystery"),("RO","Romance"),("SF","Sci-Fi"),
                          ("TH","Thriller"),("W","War"),("WS","Western")]


class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    fechaNacimiento = models.DateTimeField('fecha nacimiento')
    categoria = models.CharField(choices=categories, max_length=200)


class Director(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    biografia = models.CharField(max_length=2000)


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    año = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    resumen = models.CharField(max_length=500)
    categoria = models.CharField(choices=categories, max_length=200)



