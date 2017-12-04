from django import forms
from ckeditor_uploader.fields import RichTextUploadingFormField

from .models import Post


class PostCreateForm(forms.ModelForm):
    content = RichTextUploadingFormField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['content'].label = '内容'
        self.fields['category'].label = '版块'

    def save(self, commit=True):
        self.instance.creator = self.user
        return super().save(commit=commit)

    class Meta:
        model = Post
        fields = ('title', 'content', 'category')
