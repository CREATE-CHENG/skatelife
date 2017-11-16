from django.utils import timezone


def update_last_login(sender, request, user, **kwargs):

    ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
    user.last_ip = ip if ip else request.META['REMOTE_ADDR']

    user.save(update_fields=['last_ip'])


def update_joined(sender, request, user, **kwargs):

    ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
    user.joined_ip = ip if ip else request.META['REMOTE_ADDR']

    user.save(update_fields=['joined_ip'])
