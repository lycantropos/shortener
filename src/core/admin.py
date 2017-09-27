from django.contrib import admin

from . import models

admin.site.register(models.RawURL)
admin.site.register(models.URL)
