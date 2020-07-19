'''
https://django-filter.readthedocs.io/en/master/
'''

from apibase.filters import BaseFilter
from .. import models


class PostFilter(BaseFilter):

    class Meta:
        model = models.Post
        exclude = ['']

class PostmetaFilter(BaseFilter):

    class Meta:
        model = models.Postmeta
        exclude = ['']