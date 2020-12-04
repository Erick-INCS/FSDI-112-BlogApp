from django.views.generic import ListView, View, DetailView
from .models import Post

from django.shortcuts import render
# Create your views here.

class BlogListView(ListView):
    """
    docstring
    """
    model = Post
    template_name = 'home.html'


class BlogDetailView(ListView):
    """
    docstring
    """
    model = Post
    template_name = 'post_detail.html'