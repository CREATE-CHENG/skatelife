from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('all/', AllUserView.as_view(), name='all'),
    path('follow/<int:pk>/', FollowView.as_view(), name='follow'),
    path('un_follow/<int:pk>/', UnFollowView.as_view(), name='un_follow'),
]
