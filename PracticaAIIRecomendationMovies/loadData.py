import sys, os, django
sys.path.append("/path/to/store") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PracticaAIIMovies.settings")
django.setup()

from practica.models import *
import pandas as pd

movies = pd.read_csv('data/u.item.csv', sep="|")
users = pd.read_csv('data/u.user.csv', sep="|")
data = pd.read_csv('data/u.data.csv', sep="\t")
print(movies.head())

# for i, movie in movies.iterrows():
#     print(movie)
#     m = Pelicula.objects.get_or_create(id=movie['movie id'], titulo=movie['movie title'], fecha_estreno=movie['release date'], fecha_estreno_video=movie['video release date'], imbd_url=movie['IMDb URL'])
#
#
# for i, user in users.iterrows():
#     print(user)
#
#     u = Usuario.objects.create(id=user['id'], edad=user['age'], sexo=user['gender'], ocupacion=user['occupation'], codigo_postal=user['zip code'])
#     u.save()


for i, rating in data.iterrows():
    print(rating)
    user = Usuario.objects.get_or_create(id=rating['user_id'])
    pelicula = Pelicula.objects.get_or_create(id=rating['item_id'])

    Puntuacion.objects.get_or_create(usuario=user[0], pelicula=pelicula[0], puntuacion=rating['rating'], tiempo=rating['timestamp'])


