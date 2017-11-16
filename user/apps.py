from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        from allauth.account.signals import user_signed_up, user_logged_in
        from .receiver import update_joined, update_last_login

        user_signed_up.connect(update_joined)
        user_logged_in.connect(update_last_login)

        from .tasks import test
        test.delay()




