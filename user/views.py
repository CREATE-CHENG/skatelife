from django.views.generic import ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProfileView(TemplateView):
    template_name = 'user/profile.html'


class EmailView(TemplateView):
    template_name = 'account/email.html'


class UserDetailView(DetailView):
    pass
