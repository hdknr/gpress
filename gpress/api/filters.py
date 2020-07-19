'''
https://django-filter.readthedocs.io/en/master/
'''

import django_filters
from apibase import filters
from .. import models


class PostFilter(filters.BaseFilter):

    class Meta:
        model = models.WpPosts
        exclude = ['']

class PostmetaFilter(filters.BaseFilter):

    class Meta:
        model = models.WpPostmeta
        exclude = ['']