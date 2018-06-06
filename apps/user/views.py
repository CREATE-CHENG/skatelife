from django.views.generic import TemplateView, DetailView, View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import User
from .forms import ProfileForm

# Create your views here


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            if user.follows.filter(pk=self.kwargs.get('pk')):
                context['check_follow'] = 'followed'
        return context


class AllUserView(TemplateView):
    template_name = 'user/users.html'


class FollowView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        follower = request.user
        user = follower.follows.filter(pk=self.kwargs.get('pk')).first()
        if user:
            return JsonResponse({'res': 0})
        else:
            user = get_object_or_404(User, pk=self.kwargs.get('pk'))
            follower.follows.add(user)
            return JsonResponse({'res': 1})


class UnFollowView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        follower = request.user
        user = follower.follows.filter(pk=self.kwargs.get('pk')).first()
        if user:
            follower.follows.remove(user.pk)
            return JsonResponse({'res': 1})
        else:
            return JsonResponse({'res': 0})

