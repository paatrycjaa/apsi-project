from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='app/components/login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/components/logout/logout.html'), name='logout'),
    path('ideas', views.ideas, name='ideas'),
    path('add-idea', views.add_idea, name='add_idea'),
    path('add-opinion/<int:idea_id>/', views.add_opinion, name='add_opinion'),
    path('opinions/<int:idea_id>/', views.opinions),
    path('threads', views.threads, name = 'threads'),
    path('ajax/<ajax_request>/', csrf_exempt(views.ajax)),
    path('ajax/<ajax_request>/<int:idea_id>/', csrf_exempt(views.ajax))
    #path('ajax/<ajax_request>/<int:opinion_id>/', csrf_exempt(views.ajax))
]
