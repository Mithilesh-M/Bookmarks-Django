from django import forms
from .models import Bookmarks


class BookmarkForms(forms.ModelForm):

    class Meta:
        model = Bookmarks
        fields = ['name','url']
