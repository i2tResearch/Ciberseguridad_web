"""User Profile Model."""
from django.db import models

from audio_detector_api.utils.models import BaseModel

import os

# pylint: disable=R0903


class Audio(BaseModel):
    """Audio.

    A Audio entity that represent old results of the model


    Args:
        models.Model: Extend the BaseModel Model.
    """

    audio_file = models.FileField(
        upload_to='audios/unlabeled',
        null=False,
        blank=False,
        help_text='Audio file',
    )

    hash_text = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text='Last Predcit Result'
    )

    result = models.FloatField(
        null=True,
        blank=True,
        help_text='Last Predcit Result'
    )

    def __str__(self):
        """Return Filename."""
        return str(self.audio_file)
    
    def filename(self):
        return os.path.basename(self.audio_file.name)

    class Meta(BaseModel.Meta):
        """Meta options for Profiles."""

        db_table = 'AUDIOS'
        verbose_name = 'Audio'
        verbose_name_plural = 'Audios'


