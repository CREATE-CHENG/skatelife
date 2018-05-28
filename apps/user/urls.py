from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('all/', AllUserView.as_view(), name='all'),
    path('follow/<int:pk>/', follow, name='follow'),
    path('un_follow/<int:pk>/', un_follow, name='un_follow'),
]
