import django_filters
from .models import Bookmarks


class BookmarksFilter(django_filters.FilterSet):
    class Meta:
        model = Bookmarks
        fields = ["name"]
