import graphene
import graphene.relay
from graphene_django.types import DjangoObjectType
# https://docs.graphene-python.org/projects/django/en/latest/queries/
from apibase.schema import NodeMixin, NodeSet
from .. import models
from . import filters


class Post(NodeMixin, DjangoObjectType):
    class Meta:
        model = models.WpPosts
        filterset_class = filters.PostFilter
        interfaces = (graphene.Node, )


class Postmeta(NodeMixin, DjangoObjectType):
    class Meta:
        model = models.WpPostmeta
        filterset_class = filters.PostmetaFilter
        interfaces = (graphene.Node, )


class Query(graphene.ObjectType):
    post = graphene.relay.Node.Field(Post)
    post_set = NodeSet(Post)

    postmeta = graphene.relay.Node.Field(Postmeta)
    postmeta_set = NodeSet(Postmeta)


class Mutation(graphene.ObjectType):
    pass
