from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


def user_directory_path(instance, filename):
    return 'avatar/{0}_avatar.{1}'.format(instance.pk, filename.split('.')[-1])


class User(AbstractUser):
    nickname = models.CharField(max_length=32, unique=True, verbose_name='昵称')
    avatar = models.ImageField(upload_to=user_directory_path,
                               blank=True, verbose_name='头像')
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(128, 128)],
                                      format='JPEG',
                                      options={'quality': 100})
    signature = models.CharField(max_length=100, null=True, blank=True, verbose_name='签名')
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

    def avatar_url(self):
        if not self.avatar_thumbnail:
            return '/media/image/default_avatar.jpg'
        return self.avatar_thumbnail.url

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
