from django.urls import path, include
from .views import *

app_name = 'user'
urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
]
