from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

from forum.models import Post

# Create your models here.


class Comments(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, verbose_name='帖子', on_delete=models.SET_NULL, null=True, related_name='comments')
    content = models.TextField(verbose_name='评论内容')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name='回复时间')
    reply_to = models.ForeignKey('self', blank=True, null=True, verbose_name='@', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = verbose_name
        get_latest_by = "submit_time"

    def __str__(self):
        if self.reply_to:
            return self.creator.nickname + '@' + self.reply_to.creator.nickname
        return self.creator.nickname + '的回复'
