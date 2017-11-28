from django import template
from user.models import User
from forum.models import Category

register = template.Library()


@register.simple_tag
def latest_members(num=8):
    return User.objects.order_by('-joined_time')[:num]


@register.simple_tag
def user_count():
    return User.objects.count()


@register.simple_tag
def get_categories():
    return Category.objects.all()

