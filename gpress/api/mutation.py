from django.http import Http404
import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphql_relay import from_global_id
from apibase.schema import BaseSerializerMutation
from . import serializers


class Post(BaseSerializerMutation):
    class Meta:
        serializer_class = serializers.PostSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class Postmeta(BaseSerializerMutation):
    class Meta:
        serializer_class = serializers.PostmetaSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    post = Post.Field()
    postmeta = Postmeta.Field()
