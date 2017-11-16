from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=32, null=True, unique=True, verbose_name='昵称')
    avatar = models.ImageField(upload_to='image//%Y/%m/', blank=True, verbose_name='头像')
    signature = models.TextField(null=True, blank=True, verbose_name='签名')
    joined_time = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')
    joined_ip = models.GenericIPAddressField(null=True, blank=True)
    last_ip = models.GenericIPAddressField(null=True, blank=True, unpack_ipv4=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('user:detail', args=(self.pk,))

    def __str__(self):
        return self.username
