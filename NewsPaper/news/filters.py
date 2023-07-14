from django_filters import FilterSet, CharFilter, DateTimeFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='По заголовку')
    post_author = CharFilter(lookup_expr='icontains', label='По имени автора')
    date_created = DateTimeFilter(
        field_name='date_created',
        lookup_expr='gt',
        label='Позже указанной даты',
        widget=forms.DateTimeInput(attrs={'type': 'DATETIME'})
    )

    class Meta:
        model = Post
        fields = ['title', 'post_author', 'date_created']
