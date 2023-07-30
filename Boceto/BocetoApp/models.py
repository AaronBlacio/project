from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# La clase anterior define un modelo para una publicación de blog con campos para título, contenido, imagen, autor,
# fecha de creación y fecha de actualización.
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=200)
    contenido=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to="blog", null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo

