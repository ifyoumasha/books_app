from django_filters.rest_framework import (ChoiceFilter,
                                           FilterSet,
                                           ModelChoiceFilter)

from books.models import Category


class BookFilterSet(FilterSet):
    """Фильтрация для модели Category."""

    STATUS_CHOICES = (
        (0, 'PUBLISH'),
        (1, 'MEAP'),
    )

    book_title = ModelChoiceFilter(queryset=Category.objects.all())
    author = ModelChoiceFilter(queryset=Category.objects.all())
    status = ChoiceFilter(choices=STATUS_CHOICES)

    def is_book_title_filter(self, queryset, name, value):
        if value and not self.request.user.is_anonymous:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def is_author_filter(self, queryset, name, value):
        if value and not self.request.user.is_anonymous:
            return queryset.filter(baskets__user=self.request.user)
        return queryset

    def is_status_filter(self, queryset, name, value):
        if value and not self.request.user.is_anonymous:
            return queryset.filter(baskets__user=self.request.user)
        return queryset

    class Meta:
        model = Category
        fields = ('author', 'book_title', 'status')
