from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from braces.views import UserFormKwargsMixin
from django.http import HttpResponseForbidden
from .models import Post, Category
from .forms import PostCreateForm
from comments.forms import CommentForm
from comments.models import Comments
from . import handlers
from comments import handlers


class IndexView(ListView):
    paginate_by = 25
    model = Post
    template_name = 'forum/index.html'

    def get_queryset(self):
        return Post.order()


class PostDetailView(ModelFormMixin, DetailView):
    model = Post
    template_name = 'forum/post_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('forum:detail', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_form_kwargs(self):
        kwargs = super(ModelFormMixin, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        kwargs.update({'post': self.get_object()})
        return kwargs

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        reply_to = form.data.copy()
        if reply_to['reply_to']:
            reply_to['reply_to'] = get_object_or_404(Comments, pk=reply_to['reply_to'])
            form.data = reply_to
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PostCreateView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):
    template_name = 'forum/post_create.html'
    form_class = PostCreateForm


class CategoryView(ListView):
    paginate_by = 25
    template_name = 'forum/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        queryset = Post.order().filter(category__slug=self.kwargs['slug']).all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = Category.objects.get(slug=self.kwargs['slug']).name
        return context


class SearchView(ListView):
    paginate_by = 25
    template_name = 'forum/index.html'
    content_type = 'post_list'

    def get_queryset(self):
        query_set = Post.order().filter(title__icontains=self.request.GET['q'])
        return query_set





