"""API Queries.

Queries for GraphQL API.
"""
import graphene

# pylint: disable=too-few-public-methods,too-many-ancestors,bad-continuation
class Query(graphene.ObjectType):
    """Fronterapp API Queries."""
    dummy = graphene.Field(
        graphene.String,
        description='Get dummy query',
    )

    def resolve_dummy(root, info, **kwargs):
        # Querying a list
        return "Query dummy"
