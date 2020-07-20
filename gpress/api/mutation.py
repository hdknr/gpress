from django.http import Http404
import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphql_relay import from_global_id
from . import serializers


class Post(SerializerMutation):
    class Meta:
        serializer_class = serializers.PostSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class Postmeta(SerializerMutation):
    class Meta:
        serializer_class = serializers.PostmetaSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        client_mutation_id = input.get('client_mutation_id', None) 
        if isinstance(client_mutation_id, str):
            _, id = from_global_id(client_mutation_id)
            input['id'] = id
        return super().get_serializer_kwargs(root, info, **input)


class Mutation(graphene.ObjectType):
    post = Post.Field()
    postmeta = Postmeta.Field()
