from audio_detector_api.audios.models import Audio
from django.contrib import admin


class AudioAdmin(admin.ModelAdmin):
    """Configuration for Audios module.

    Audio admin config.
    """

    list_display = ('audio_file',)
    list_filter = ('audio_file', 'result', 'created', 'modified')
    date_hierarchy = 'created'
    list_per_page = 10



admin.site.register(Audio, AudioAdmin)