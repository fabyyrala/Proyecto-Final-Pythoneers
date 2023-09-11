from django.contrib import admin
from .models import Post, Categoria, Comentario

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id","titulo", "contenido", "resumen", "fecha_creacion", "autor", "imagen", "publicado", "categoria", "fecha_actualizacion", "permitir_comentarios")


admin.site.register(Categoria)
admin.site.register(Comentario)