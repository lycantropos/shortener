from django import forms
from django.core.handlers.wsgi import WSGIRequest

from . import models
from .utils import shorten


class URL(forms.Form):
    original = forms.URLField(label='original URL')

    @classmethod
    def from_request(cls, request: WSGIRequest):
        if request.method == 'POST':
            form = cls(request.POST)
            if form.is_valid():
                original_url = form.cleaned_data['original']
                short_url = request.build_absolute_uri(shorten(original_url))
                try:
                    url = generate_url(original_url, short_url)
                except Exception as err:
                    form.add_error(field=None,
                                   error=err)
                else:
                    url.save()
        else:
            form = cls()
        return form


def generate_url(original_url: str,
                 short_url: str) -> models.URL:
    original = models.RawURL.objects.create(address=original_url)
    short = models.RawURL.objects.create(address=short_url)
    return models.URL.objects.create(original=original,
                                     short=short)
