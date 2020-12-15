from django.conf.urls import url
from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ideas$', views.ideas, name='ideas'),
    url(r'^add-idea$', views.add_idea, name='add_idea'),
    path('opinions/<int:idea_id>/', views.opinions),
    path('ajax/<ajax_request>/', csrf_exempt(views.ajax)),
    path('ajax/<ajax_request>/<int:idea_id>/', csrf_exempt(views.ajax))
]
