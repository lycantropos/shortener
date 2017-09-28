from django.conf.urls import url
from django.contrib.auth import views as auth_views

from core import views as core_views

urlpatterns = [
    url(r'^$', core_views.home,
        name='home'),
    url(r'^\w{6}$', core_views.redirect_shorten,
        name='redirect_shorten'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'},
        name='logout'),
    url(r'^signup/$', core_views.signup,
        name='signup'),
]
