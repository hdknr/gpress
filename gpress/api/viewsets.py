from rest_framework import (
    viewsets, pagination, response, decorators)
from . import serializers, filters, permissions
from .. import models


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.Permission, ]
    filter_class = filters.PostFilter
    serializer_class = serializers.PostSerializer
    queryset = models.WpPosts.objects.all()

