from django import forms
from . import models

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = models.Comentario
        fields = ['contenido']

class CrearPostForm(forms.ModelForm):
    # autor = forms.ModelChoiceField(queryset=models.User.objects.all(), empty_label="seleccionar autor")
    categoria = forms.ModelChoiceField(queryset=models.Categoria.objects.all(), empty_label="seleccionar categoria")
    class Meta:
        model = models.Post
        fields = ['titulo', 'contenido', 'resumen', 'imagen', 'categoria', 'permitir_comentarios' ]
   

class NewCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = '__all__'