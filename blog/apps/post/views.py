from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post, Comentario, Categoria
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ComentarioForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CrearPostForm, NewCategoriaForm
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404

######### VISTAS DE POSTS #########
class PostsListView(ListView):
    model = Post
    template_name = "post/posts.html"
    context_object_name = "posts"
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        order = self.request.GET.get("orden")
        if order == "reciente":
            queryset = queryset.order_by("-fecha_creacion")
        elif order == "antiguo":
            queryset = queryset.order_by("fecha_creacion")
        elif order == "alfabetico_asc":
            queryset = queryset.annotate(lower_title=Lower("titulo")).order_by("lower_title")
        elif order == "alfabetico_desc":
            queryset = queryset.annotate(lower_title=Lower("titulo")).order_by("-lower_title")
        selected_name_category = self.request.GET.get("categoria")
        if selected_name_category is not None:
            if selected_name_category == "todos":
                return queryset
            categoria = get_object_or_404(Categoria, titulo=selected_name_category)
            queryset = queryset.filter(categoria=categoria)
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orden"] = self.request.GET.get("orden", 'reciente')
        context["categorias"] = Categoria.objects.all()
        return context
    


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = "post" ##fijarse si no es posts
    pk_url_kwarg = "id" #se encarga de obtener el id del post en la url
    queryset = Post.objects.all() #se encarga de obtener los datos del post en la base de datos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ComentarioForm()
        context["comentarios"] = Comentario.objects.filter(post_id=self.kwargs['id'])
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            new_comentario = form.save(commit=False)
            new_comentario.user = request.user
            new_comentario.post_id = self.kwargs['id']
            new_comentario.save()
            return redirect("post:post_detail", id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)
        
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CrearPostForm
    template_name = "post/new_post.html"
    success_url = reverse_lazy("post:posts")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.autor = self.request.user
        post.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = CrearPostForm
    template_name = "post/edit_post.html"
    success_url = reverse_lazy("post:posts")

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post/delete_post.html"
    success_url = reverse_lazy("post:posts")


######### VISTAS DE COMENTARIOS #########
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = "comentarios/new_comentario.html"
    success_url = "comentarios/comentario"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['id']
        return super().form_valid(form)
    

class ComentarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = "comentarios/edit_comentario.html"
    
    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url is not None:
            return next_url
        else:
            return reverse_lazy("post:post_detail", args=[self.object.post.id])
        

class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = "comentarios/delete_comentario.html"
    
    def get_success_url(self):
        return reverse_lazy("post:post_detail", args=[self.object.post.id])
    

######### VISTAS DE CATEGORIAS #########
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = NewCategoriaForm
    template_name = "post/new_categoria.html"
    
    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url is not None:
            return next_url
        else:
            return reverse_lazy("post:new_post")
        
class CategoriaListView(ListView):
    model = Categoria
    template_name = "post/list_categoria.html"
    context_object_name = "categorias"


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "post/confirm_delete_categoria.html"
    success_url = reverse_lazy("post:list_categoria")


######### VISTAS DE FILTROS #########
class PostByCategoryView(ListView):
    model = Post
    template_name = "post/post_by_category.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        return Post.objects.filter(categoria_id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoria"] = Categoria.objects.get(pk=self.kwargs['pk'])
        return context
    