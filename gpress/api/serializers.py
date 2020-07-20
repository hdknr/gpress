from rest_framework import serializers
from apibase.serializers import BaseModelSerializer
from .. import models
from logging import getLogger
logger = getLogger()


class PostSerializer(BaseModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        valid = super().is_valid(raise_exception=raise_exception)
        if self._errors:
            for key, e in self._errors.items():
                logger.debug(f"*****{key}:{e}")
        return valid

    def create(self, validated_data):
        logger.debug(f"create....{validated_data}")
        return super().create(validated_data)


class PostmetaSerializer(BaseModelSerializer):
    meta_value_obj = serializers.JSONField(read_only=True)
    class Meta:
        model = models.Postmeta
        fields = '__all__'
