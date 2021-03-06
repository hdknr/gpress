import graphene
from gpress.api import (
    query as gpress_query, mutation as gpress_mutation, )


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


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    auto_camelcase=False,
)
