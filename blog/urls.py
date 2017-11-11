from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/', ArticleDetailView.as_view(), name='detail'),
]