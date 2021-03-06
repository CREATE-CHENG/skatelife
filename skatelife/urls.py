"""skatelife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),
    path('', include('allauth.urls')),
    path('user/', include('user.urls')),
    path('notifications/', include(notifications.urls, namespace='notifications')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
