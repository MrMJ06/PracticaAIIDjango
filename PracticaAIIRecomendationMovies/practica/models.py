from django.db import models


# Create your models here.
class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    fecha_estreno = models.CharField(max_length=200)
    fecha_estreno_video = models.CharField(max_length=200)
    imbd_url = models.CharField(max_length=200)
    #categorias = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.titulo



class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=200)
    ocupacion = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=200)




class Puntuacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    tiempo = models.IntegerField()

    def __str__(self):
        return str(self.puntuacion) + " "+ str(self.pelicula.id)