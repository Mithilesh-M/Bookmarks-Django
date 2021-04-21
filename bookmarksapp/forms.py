from django import forms
from .models import Bookmarks, Folder


class BookmarkForms(forms.ModelForm):

    class Meta:
        model = Bookmarks
        fields = ['name','url','description','tags','folder']

class FolderForm(forms.ModelForm):

    class Meta:
        model = Folder
        fields = ['name']