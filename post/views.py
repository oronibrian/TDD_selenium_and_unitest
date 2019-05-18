from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    template_name = 'home.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

