from django.contrib import admin
from .models import Pelicula, Director, Usuario

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Usuario)