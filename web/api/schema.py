import graphene
from gpress.api import (
    query as gpress_query,
    mutation as gpress_mutation,
    subscriptions as gress_subs, )

from .consumers import GraphqlWsConsumer


class Query(
    gpress_query.Query,
    graphene.ObjectType
):
    pass

class Mutation(
    gpress_mutation.Mutation,
    graphene.ObjectType
):
    pass

class Subscription(
    gress_subs.Subscription,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription,
    auto_camelcase=False,
)


class SchemaWsConsumer(GraphqlWsConsumer):
    schema = schema
