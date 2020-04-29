from rest_framework import (
    viewsets, response, decorators)
from . import serializers, filters, permissions, paginations
from .. import models


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.Permission, ]
    filter_class = filters.PostFilter
    serializer_class = serializers.PostSerializer
    queryset = models.WpPosts.objects.all()
    pagination_class = paginations.Pagination

