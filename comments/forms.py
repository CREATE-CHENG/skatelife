from django import forms
from ckeditor_uploader.fields import RichTextUploadingFormField

from .models import Comments


class CommentForm(forms.ModelForm):
    content = RichTextUploadingFormField()
    reply_to = forms.ChoiceField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ''

    def save(self, commit=True):
        self.instance.creator = self.user
        self.instance.post = self.post
        return super().save(commit=commit)

    class Meta:
        model = Comments
        fields = ('content', 'reply_to')
