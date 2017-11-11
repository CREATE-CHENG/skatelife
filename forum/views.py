from django.shortcuts import render
from django.views.generic import DetailView, ListView


def index(request):
    return render(request, 'forum/index.html')


class PostDetailView(DetailView):
    pass


class CategoryView(ListView):
    pass
