from django.conf.urls import url
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ideas$', views.ideas, name='ideas'),
    url(r'^add-idea$', views.add_idea, name='add_idea'),
    url(r'^opinions$', views.opinions, name='opinions'),
    url(r'^ajax/(?P<ajax_request>\w+)/$', csrf_exempt(views.ajax), name='ajax')
]
