from django.shortcuts import render
from .models import Bookmarks, Folder
from .filters import BookmarksFilter
from .forms import BookmarkForms, FolderForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    """View function for home page of site."""

    bookmarks = Bookmarks.objects.all()
    namefilter = BookmarksFilter(request.GET, queryset=bookmarks)
    folder_list = Folder.objects.all()
    if(request.POST):
        bookmarkform = BookmarkForms(request.POST)
        folderform = FolderForm(request.POST)
    else:
        bookmarkform = BookmarkForms(initial={'url':'https://www.'})
        folderform = FolderForm()
    if (bookmarkform.is_valid()):
        bookmarkform.save()
    if (folderform.is_valid()):
        folderform.save()
    context = {
        'filter': namefilter,
        'folder_list': folder_list,
        'bookmarkform': bookmarkform,
        'folderform': folderform,
    }
    return render(request, 'bookmarks.html', context=context)


def Deletebookmarks(request,pk):
    Bookmarks.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('index'))



