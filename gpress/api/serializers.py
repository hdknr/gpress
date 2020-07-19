from rest_framework import serializers
from apibase.serializers import BaseModelSerializer
from .. import models


class PostSerializer(BaseModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class PostmetaSerializer(BaseModelSerializer):
    meta_value_obj = serializers.JSONField(read_only=True)
    class Meta:
        model = models.Postmeta
        fields = '__all__'
