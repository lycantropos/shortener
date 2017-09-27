from django.db.models import QuerySet

from . import models


def get_url_by_short(short: str) -> QuerySet:
    return models.URL.objects.select_related().filter(short__address=short)
