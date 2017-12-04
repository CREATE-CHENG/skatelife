from django.db import models

from user.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='板块名称', unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('forum:category', args=(self.slug,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '板块'
        verbose_name_plural = verbose_name


class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='创建者', null=True)
    title = models.CharField(max_length=128, verbose_name='帖子标题')
    content = models.TextField(verbose_name='帖子内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = verbose_name
        ordering = ['created_time']   # 回复功能增加后修改为按回复时间排序

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('forum:detail', args=(self.pk,))

    def latest_time(self):
        if self.comments.count():
            return self.comments.latest().submit_time
        return self.created_time
