import django_filters
from .models import Bookmarks


class BookmarksFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Bookmarks
        fields = ["name"]
