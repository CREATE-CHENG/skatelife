from django.db import models
from django.conf import settings

from forum.models import Post

# Create your models here.


class Comments(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, verbose_name='帖子', on_delete=models.SET_NULL, null=True)
    content = models.TextField(verbose_name='评论内容')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name='回复时间')

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.creator.nickname + '的回复'
