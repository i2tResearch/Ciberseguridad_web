"""Audio Structure GraphQL."""
import graphene
from graphene_django.types import DjangoObjectType

from audio_detector_api.audios.models import Audio


class AudioType(DjangoObjectType):
    """Audio Type."""

    # pylint: disable=unused-argument,too-few-public-methods

    result = graphene.Field(
        graphene.Float,
        description='Get last result',
    )

    hash_text = graphene.Field(
        graphene.String,
        description='Get hash File',
    )

    def resolve_result(self, args):
        """Get result of the audio."""
        return self.result

    def resolve_hash_text(self, args):
        """Get hash of the audio."""
        return self.hash_text

    def resolve_audio_file(self, args):
        """Get hash of the audio."""
        return self.filename()

    class Meta:
        """Meta Information for ProfileType."""

        model = Audio
        description = 'Audios'
        only_fields = (
            'id',
            'result',
            "hash_text",
            'audio_file',
        )
