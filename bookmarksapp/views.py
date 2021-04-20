from django.shortcuts import render
from .models import Bookmarks
from .filters import BookmarksFilter

def index(request):
    """View function for home page of site."""

    bookmarks = Bookmarks.objects.all()
    filter = BookmarksFilter(request.GET, queryset=bookmarks)

    context = {
        'filter':filter
    }

    return render(request, 'bookmarks.html', context=context)
