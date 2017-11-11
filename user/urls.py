from django.urls import path, include
from .views import *


urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email/', EmailView.as_view(), name='email'),
    path('<int:year>/', UserDetailView.as_view(), name='detail')
]