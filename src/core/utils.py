from django.core.paginator import (Page,
                                   Paginator,
                                   PageNotAnInteger,
                                   EmptyPage)
from django.db.models import QuerySet
from hashlib import sha256


def shorten(url: str) -> str:
    return sha256(url.encode()).hexdigest()[:6]


def paginate(objects: QuerySet,
             *,
             page_number: int,
             per_page: int = 25) -> Page:
    paginator = Paginator(objects,
                          per_page=per_page)
    try:
        objects = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    return objects
