from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    nickname = models.CharField(max_length=32, null=True, unique=True)
    avatar = models.ImageField(upload_to='', blank=True, verbose_name='头像')
    joined_time = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')
    joined_ip = models.GenericIPAddressField()
    last_ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return '{}的配置。'.format(self.user.username)

    class Meta:
        verbose_name = '用户配置'
        verbose_name_plural = verbose_name
