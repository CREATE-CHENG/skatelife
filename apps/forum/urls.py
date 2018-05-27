from django.urls import path
from .views import *

app_name = 'forum'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/edit/', PostCreateView.as_view(), name='post_create'),
]
