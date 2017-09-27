from django.contrib.auth import (login,
                                 authenticate)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import (render,
                              redirect,
                              get_object_or_404)

from . import (models,
               forms)
from .data_access import get_url_by_short
from .utils import paginate


@login_required
def home(request: WSGIRequest) -> HttpResponse:
    form = forms.URL.from_request(request)
    page_number = request.GET.get('page')
    urls = (models.URL.objects
            .order_by(models.URL.created_timestamp.field_name)
            .reverse()
            .all())
    urls = paginate(urls,
                    page_number=page_number)
    context = {'form': form,
               'urls': urls}
    return render(request, 'home.html', context)


def redirect_shorten(request: WSGIRequest) -> HttpResponse:
    short_url = request.get_raw_uri()
    url: models.URL = get_object_or_404(get_url_by_short(short_url))
    url.counter += 1
    url.save()
    return redirect(url.original.address)


def signup(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)
