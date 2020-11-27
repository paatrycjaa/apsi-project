from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ideas$', views.ideas, name='ideas'),
    url(r'^add-idea$', views.add_idea, name='add_idea'),
    url(r'^ajax/(?P<ajax_request>\w+)/$', views.ajax, name='ajax')
]
