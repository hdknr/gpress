import graphene
from gpress.api import schema as gpress_schema


class Query(
    gpress_schema.Query,
):
    pass


schema = graphene.Schema(
    query=Query,
    auto_camelcase=False,
)
