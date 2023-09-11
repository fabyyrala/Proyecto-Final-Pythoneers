from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class Categoria(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.titulo
    
class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True, null=False)
    contenido = models.TextField(null=False)
    resumen = models.TextField(max_length=600, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="media/", null=False)
    publicado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    permitir_comentarios = models.BooleanField(default=True)

    class Meta:
        ordering = ("-publicado",)
        
    def __str__(self):
        return self.titulo
    
    def delete(self, *args):
        self.imagen.delete()
        super().delete(*args)


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios', default=1)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contenido
    
    class Meta:
        ordering = ["-fecha_creacion"]

    def delete(self, *args):
        super().delete(*args)