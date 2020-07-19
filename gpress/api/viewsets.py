from rest_framework import viewsets
from . import serializers, filters, permissions
from .. import models
from apibase import paginations


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    permission_classes = [permissions.Permission, ]
    filter_class = filters.PostFilter
    serializer_class = serializers.PostSerializer
    pagination_class = paginations.Pagination


class PostmetaViewSet(viewsets.ModelViewSet):
    queryset = models.Postmeta.objects.all()
    permission_classes = [permissions.Permission, ]
    filter_class = filters.PostmetaFilter
    serializer_class = serializers.PostmetaSerializer
    pagination_class = paginations.Pagination
