from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:id>/', PostDetailView.as_view(), name='detail'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category')
]