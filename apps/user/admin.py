from django.contrib import admin
from .models import User
from imagekit.admin import AdminThumbnail


class AvatarAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='avatar_thumbnail')


admin.site.register(User, AvatarAdmin)

