# Generated by Django 2.0 on 2018-12-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='fecha_estreno',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='fecha_estreno_video',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='imbd_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
