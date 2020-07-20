import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from . import serializers


class Post(SerializerMutation):
    class Meta:
        serializer_class = serializers.PostSerializer
        model_operations = ['create', 'update']
        # lookup_field = 'id'


class Mutation(graphene.ObjectType):
    post = Post.Field()