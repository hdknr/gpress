import graphene
import graphene.relay
from graphene_django.types import DjangoObjectType
# https://docs.graphene-python.org/projects/django/en/latest/queries/
from graphene_django.filter import DjangoFilterConnectionField

from .. import models
from . import filters, serializers



class NodeMixin(object):
    # self: Model Class

    pk = graphene.Int()
    endpoint = graphene.String()

    def resolve_pk(self, info):
        return self.pk

    def resolve_endpoint(self, info):
        path = serializers.drf_endpoint(self)
        if hasattr(info.context, 'build_absolute_uri'):
            return info.context.build_absolute_uri(path)
        return path

    @classmethod
    def get_node(cls, info, id):
        queryset = cls.get_queryset(cls._meta.model.objects, info)
        try:
            return queryset.get(pk=id)
        except cls._meta.model.DoesNotExist:
            return None


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
    post_set = DjangoFilterConnectionField(Post)

    postmeta = graphene.relay.Node.Field(Postmeta)
    postmeta_set = DjangoFilterConnectionField(Postmeta)


class Mutation(graphene.ObjectType):
    pass
