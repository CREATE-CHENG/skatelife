from django.db import models
from user.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    user = models.ForeignKey(User, related_name='posts', verbose_name='用户')
    content = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog', args=[self.pk])

    def __str__(self):
        return self.title
