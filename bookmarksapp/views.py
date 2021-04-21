from django.shortcuts import render
from .models import Bookmarks
from .filters import BookmarksFilter
from .forms import BookmarkForms
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    """View function for home page of site."""

    bookmarks = Bookmarks.objects.all()
    namefilter = BookmarksFilter(request.GET, queryset=bookmarks)
    if(request.POST):
        bookmarkform = BookmarkForms(request.POST)
    else:
        bookmarkform = BookmarkForms(initial={'url':'https://www.'})
    if (bookmarkform.is_valid()):
        bookmarkform.save()
    context = {
        'filter': namefilter,
        'bookmarkform': bookmarkform
    }
    return render(request, 'bookmarks.html', context=context)


def Deletebookmarks(request,pk):
    Bookmarks.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('index'))



