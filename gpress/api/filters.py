'''
https://django-filter.readthedocs.io/en/master/
'''

import django_filters
from .. import models


class PostFilter(django_filters.FilterSet):

    class Meta:
        model = models.WpPosts
        exclude = ['']

class PostmetaFilter(django_filters.FilterSet):

    class Meta:
        model = models.WpPostmeta
        exclude = ['']