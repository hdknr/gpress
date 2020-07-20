from django.http import Http404
import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from . import serializers


class Post(SerializerMutation):
    class Meta:
        serializer_class = serializers.PostSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    post = Post.Field()

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        if 'id' in input:
            instance = Post.objects.filter(id=input['id']).first()
            if instance:
                return {'instance': instance, 'data': input, 'partial': True}
            else:
                raise Http404

        return {'data': input, 'partial': False}