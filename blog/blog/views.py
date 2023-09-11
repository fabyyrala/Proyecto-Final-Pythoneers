from django.shortcuts import render
from apps.post.models import Post


def index(request):
    recent_posts = Post.objects.all().order_by('-fecha_creacion')[:4]
    context = {
        'recent_posts': recent_posts
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def page_not_found(request, exception):
    return render(request, '404.html')