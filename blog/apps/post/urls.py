from django.urls import path
from . import views


app_name = "post" # le damos un nombre a la app para evitar hardcodear en los templates
urlpatterns = [
    path("", views.PostsListView.as_view(), name="posts"),
    path("<int:id>/", views.PostDetailView.as_view(), name="post_detail"),
    path("new_post/", views.PostCreateView.as_view(), name="new_post"),
    path("<int:pk>/edit", views.PostUpdateView.as_view(), name="edit_post"),
    path("<int:pk>/delete", views.PostDeleteView.as_view(), name="delete_post"),
    path("new_categoria/", views.CategoriaCreateView.as_view(), name="new_categoria"),
    path("list_categoria/", views.CategoriaListView.as_view(), name="list_categoria"),
    path("list_categoria/<int:pk>/delete", views.CategoriaDeleteView.as_view(), name="delete_categoria"),
    path("comentario/<int:pk>/delete", views.ComentarioDeleteView.as_view(), name="delete_comentario"),
    path("comentario/<int:pk>/update", views.ComentarioUpdateView.as_view(), name="edit_comentario"),
    path("categoria/<int:pk>/posts", views.PostByCategoryView.as_view(), name="post_by_category"),
    ]