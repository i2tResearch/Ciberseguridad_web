"""User Login Mutations."""
import graphene

from graphene_file_upload.scalars import Upload
import hashlib

from audio_detector_api.model_predict.inference import predict

import os

from django.conf import settings


from audio_detector_api.schema.audios.audios_type import AudioType

from audio_detector_api.audios.models import Audio

from keras import backend as K


class AudioPredict(graphene.Mutation):
    """Mutation for Predict a Audio."""

    # pylint: disable=too-few-public-methods,no-self-argument,unused-argument

    class Arguments:
        """Predict an audio file."""
        # Audio File
        audio_file = Upload(required=True)

    audio_file = graphene.Field(AudioType)

    def mutate(root, info, **kwargs):
        """Mutation method."""
        # pylint: disable=no-self-use
        audio_file = kwargs.get('audio_file', None)

        audio = Audio(
            audio_file=audio_file,
        )

        audio.save()

        print(audio.filename())

        hash_calculated = md5(audio.filename())

        K.clear_session()

        predict_label = predict()

        K.clear_session()

        audio.hash_text = hash_calculated
        audio.result = predict_label

        audio.save()

        os.remove(os.path.join(settings.MEDIA_ROOT,
                  "audios", "unlabeled", audio.filename()))

        return AudioPredict(audio_file=audio)


def md5(fname):
    hash_md5 = hashlib.md5()
    with open("media/audios/unlabeled/"+fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
