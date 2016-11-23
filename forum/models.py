from django.db import models
from user.models import User

# Create your models here.


class Plate(models.Model):
    name = models.CharField(max_length='64', verbose_name='板块名称')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')


class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建者')
    title = models.CharField(max_length=128, verbose_name='帖子标题')
    content = models.TextField(verbose_name='帖子内容')
    user = models.ForeignKey(User, verbose_name='创建者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')
    plate = models.ForeignKey(Plate, related_name='posts')

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
