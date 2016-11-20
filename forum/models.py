from django.db import models
from user.models import User

# Create your models here.


class Plate(models.Model):
    name = models.CharField(max_length='64', verbose_name='板块名称')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='帖子标题')
    content = models.TextField(verbose_name='帖子内容')
    user = models.ForeignKey(User, verbose_name='创建者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')
    plate = models.ForeignKey(Plate, related_name='posts')
