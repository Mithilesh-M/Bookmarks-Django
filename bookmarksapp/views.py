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
        return HttpResponseRedirect(reverse('index'))
    if (folderform.is_valid()):
        folderform.save()
        return HttpResponseRedirect(reverse('index'))
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
    context = {
        'folder_list': folder_list,
        'bookmark': bookmark,
    }
    return render(request, 'bookmarksapp/detail_bookmark.html', context=context)

def Updatebookmarks(request,pk):
    """View function for Detail bookmark"""
    folder_list = Folder.objects.all()
    bookmark = get_object_or_404(Bookmarks,pk=pk)
    if (request.POST):
        bookmarkform = BookmarkForms(request.POST,instance=bookmark)
    else:
        bookmarkform = BookmarkForms(initial={'name':bookmark.name,'url':bookmark.url,'description':bookmark.description,'folder':bookmark.folder,'tags':bookmark.tags.all})
    if(bookmarkform.is_valid()):
        bookmarkform.save()
        return HttpResponseRedirect(reverse('index'))
    context = {
        'folder_list': folder_list,
        'form': bookmarkform,
        'bookmark': bookmark,
    }
    return render(request, 'bookmarksapp/update_bookmark.html', context=context)


def FolderList(request,pk):
    """View function for list Folder bookmark"""
    folder = get_object_or_404(Folder, pk=pk)
    bookmarks = folder.bookmarks_set.all()
    namefilter = BookmarksFilter(request.GET, queryset=bookmarks)
    folder_list = Folder.objects.all()
    if (request.POST):
        bookmarkform = BookmarkForms(request.POST)
        folderform = FolderForm(request.POST)
    else:
        bookmarkform = BookmarkForms(initial={'url': 'https://www.'})
        folderform = FolderForm()
    if (bookmarkform.is_valid()):
        bookmarkform.save()
        return HttpResponseRedirect(reverse('index'))
    if (folderform.is_valid()):
        folderform.save()
        return HttpResponseRedirect(reverse('index'))
    context = {
        'filter': namefilter,
        'folder_list': folder_list,
        'folder': folder,
        'bookmarkform': bookmarkform,
        'folderform': folderform,
    }
    return render(request, 'bookmarksapp/list_folder.html', context=context)

def FolderListUnknown(request):
    """View function for list Folder bookmark"""
    folder_list = Folder.objects.all()
    folder = Bookmarks.objects.filter(folder=None)
    context = {
        'folder_list': folder_list,
        'folder': folder,
    }
    return render(request, 'bookmarksapp/list_folder_unknown.html', context=context)

def Deletefolder(request,pk):
    Folder.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('index'))


def Updatefolder(request,pk):
    """View function for Detail bookmark"""
    folder_list = Folder.objects.all()
    folder = get_object_or_404(Folder,pk=pk)
    if (request.POST):
        folderform = FolderForm(request.POST, instance=folder)
    else:
        folderform = FolderForm(initial={'name':folder.name})
    if(folderform.is_valid()):
        folderform.save()
        return HttpResponseRedirect(reverse('list-folder',args=[pk]))
    context = {
        'folder_list': folder_list,
        'form': folderform,
        'folder': folder,
    }
    return render(request, 'bookmarksapp/update_folder.html', context=context)
