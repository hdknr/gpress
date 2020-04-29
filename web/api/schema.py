import graphene
from gpress.api import schema as gpress_schema


class Query(
    gpress_schema.Query,
):
    pass


# class Mutation(
#     fulfills_schema.Mutation,
#     vendors_schema.Mutation,
#     packages_schema.Mutation,
#     graphene.ObjectType
# ):
#     pass


schema = graphene.Schema(
    query=Query,
    # mutation=Mutation,
    auto_camelcase=False,
)
