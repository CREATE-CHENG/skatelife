from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import User


# Create your views here.


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'user/profile.html'
    fields = ['nickname', 'signature', 'avatar']
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)


class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = slug_field
    template_name = 'user/detail.html'

