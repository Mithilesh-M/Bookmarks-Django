from django.shortcuts import render
from .models import Bookmarks, Folder
from .filters import BookmarksFilter
from .forms import BookmarkForms, FolderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404


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
    return render(request, 'bookmarksapp/index.html', context=context)


def Deletebookmarks(request,pk):
    Bookmarks.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('index'))


def Detailbookmarks(request,pk):
    """View function for Detail bookmark"""
    folder_list = Folder.objects.all()
    bookmark = get_object_or_404(Bookmarks,pk=pk)
    if (request.POST):
        bookmarkform = BookmarkForms(request.POST)
        folderform = FolderForm(request.POST)
    else:
        bookmarkform = BookmarkForms(initial={'url': 'https://www.'})
        folderform = FolderForm()
    if (bookmarkform.is_valid()):
        bookmarkform.save()
    if (folderform.is_valid()):
        folderform.save()
    context = {
        'folder_list': folder_list,
        'bookmarkform': bookmarkform,
        'folderform': folderform,
        'bookmark': bookmark,
    }
    return render(request, 'bookmarksapp/detail_bookmark.html', context=context)


