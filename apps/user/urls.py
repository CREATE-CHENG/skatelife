from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('all/', AllUserView.as_view(), name='all'),
]
