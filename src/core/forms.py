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
                original = models.RawURL(address=original_url)
                short = models.RawURL(address=short_url)
                try:
                    original.save(force_insert=True)
                    short.save(force_insert=True)
                except Exception as err:
                    form.add_error(field=None,
                                   error=err)
                else:
                    models.URL.objects.create(original=original,
                                              short=short)
        else:
            form = cls()
        return form
