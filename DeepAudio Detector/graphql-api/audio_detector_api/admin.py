"""Admin Site Configuration.

Setup admin settings.
"""
from django.contrib import admin

# Project configurations
admin.site.site_header = 'Audio Detector'
admin.site.site_title = 'Audio Detector'
admin.site.index_title = 'Audio Detector'
admin.empty_value_display = '**Vacio**'