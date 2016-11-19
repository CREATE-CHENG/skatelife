from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        pass

