from django.db.models.signals import post_save
from notifications.signals import notify

from .models import Comments


def comment_handler(sender, instance, created, **kwargs):
    if instance.creator != instance.post.creator:
        notify.send(instance.creator, recipient=instance.post.creator,
                    verb='发表了评论', action_object=instance,
                    target=instance.post, description=instance.content)


post_save.connect(comment_handler, sender=Comments)
