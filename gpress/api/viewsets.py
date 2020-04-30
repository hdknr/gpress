from rest_framework import (
    viewsets, response, decorators)
from . import serializers, filters, permissions, paginations
from .. import models


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.WpPosts.objects.all()
    # permission_classes = [permissions.Permission, ]
    filter_class = filters.PostFilter
    serializer_class = serializers.PostSerializer
    pagination_class = paginations.Pagination


class PostmetaViewSet(viewsets.ModelViewSet):
    queryset = models.WpPostmeta.objects.all()
    # permission_classes = [permissions.Permission, ]
    filter_class = filters.PostmetaFilter
    serializer_class = serializers.PostmetaSerializer
    pagination_class = paginations.Pagination
