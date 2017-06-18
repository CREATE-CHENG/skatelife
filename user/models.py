from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=32, null=True, unique=True)
    avatar = models.ImageField(upload_to='', blank=True, verbose_name='头像')
    joined_time = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')
    joined_ip = models.GenericIPAddressField(null=True, blank=True)
    last_ip = models.GenericIPAddressField(null=True, blank=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        pass