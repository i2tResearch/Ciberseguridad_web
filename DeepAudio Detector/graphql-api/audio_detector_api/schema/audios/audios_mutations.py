"""Audios GraphQL Mutations."""
import graphene

from audio_detector_api.schema.audios.mutations import AudioPredict


# pylint: disable=too-few-public-methods
class AudiosMutation(graphene.ObjectType):
    """Audios Mutations for GraphQL."""

    audio_predict = AudioPredict.Field()
