"""AudioDetector Main Schema."""
import graphene

from audio_detector_api.schema import Mutation as SchemeMutation

from audio_detector_api.schema import Query as SchemaQuery


# pylint: disable=too-few-public-methods


class Query(SchemaQuery, graphene.ObjectType):
    """The root of the query for Fronterapp API.

    Args:
        Query (Query): Fronterapp application queries.
        graphene (ObjectType): GraphQL types.
    """

    # pylint: disable=unnecessary-pass
    pass


# pylint: disable=too-few-public-methods

class Mutation(SchemeMutation, graphene.ObjectType):
    """Root scheme for Mutations of Audio Detection API.

    Args:
        SchemeMutation (Mutation): Audio Detection aplication Mutations
        graphene (ObjectType): GraphQL types.
    """

    # pylint: disable=unnecessary-pass
    pass




schema = graphene.Schema(
    query=Query,
    mutation=Mutation
) 


