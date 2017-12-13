from django.conf.urls import url
from .views import *

app_name = 'user'
urlpatterns = [
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'all/$', AllUserView.as_view(), name='detail'),
]
