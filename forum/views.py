from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post


class IndexView(ListView):
    paginate_by = 30
    model = Post
    template_name = 'forum/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post_detail.html'


class CategoryView(ListView):
    paginate_by = 30


