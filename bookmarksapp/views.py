from django.shortcuts import render
from .models import Bookmarks
from .filters import BookmarksFilter
from .forms import BookmarkForms


def index(request):
    """View function for home page of site."""

    bookmarks = Bookmarks.objects.all()
    namefilter = BookmarksFilter(request.GET, queryset=bookmarks)
    form = BookmarkForms(request.POST or None)
    if (form.is_valid()):
        form.save()

    context = {
        'filter': namefilter,
        'form': form
    }

    return render(request, 'bookmarks.html', context=context)
