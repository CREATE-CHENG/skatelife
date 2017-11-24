from django.forms import ModelForm
from .models import User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'signature', 'avatar']
