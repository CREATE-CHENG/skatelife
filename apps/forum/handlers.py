from django.db.models.signals import post_save
from notifications.signals import notify

from .models import Post


# 测试发帖通知，用户关注功能完成后完善此通知
def post_handler(sender, instance, created, **kwargs):

    notify.send(instance.creator, recipient=instance.creator,
                verb='发表了帖子', action_object=instance,
                target=instance, description=instance.content)


post_save.connect(post_handler, sender=Post)
