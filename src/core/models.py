from datetime import datetime

from django.db import models


class RawURL(models.Model):
    address = models.URLField(unique=True)


class URL(models.Model):
    original = models.OneToOneField(RawURL,
                                    on_delete=models.CASCADE,
                                    to_field=RawURL.address.field_name,
                                    related_name='original')
    short = models.OneToOneField(RawURL,
                                 on_delete=models.CASCADE,
                                 to_field=RawURL.address.field_name,
                                 related_name='short')
    counter = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(default=datetime.utcnow)
