from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import User
from .forms import ProfileForm

# Create your views here.
from django.contrib.auth import get_user


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'user/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)

    def form_valid(self, form):
        if 'avatar' in form.changed_data:
            self.request.user.avatar.delete(save=False)
        return super().form_valid(form)


class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = slug_field
    template_name = 'user/detail.html'
    context_object_name = 'user_detail'

