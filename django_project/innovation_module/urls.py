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
    path('my-ideas', views.my_ideas, name='my-ideas'),
    path('add-idea', views.add_idea, name='add_idea'),
    path('edit-idea/<int:idea_id>/', views.edit_idea, name='edit_idea'),
    path('add-opinion/<int:idea_id>/', views.add_opinion, name='add_opinion'),
    path('edit-opinion/<int:opinion_id>/', views.edit_opinion, name='edit_opinion'),
    path('opinions/<int:idea_id>/', views.opinions),
    path('ideasfiltered/<str:status_pomyslu>/', views.ideasfiltered, name='ideasfiltered'),
    path('add_decision/<int:idea_id>/', views.add_decision, name='add_decision'),
    path('posts/<int:thread_id>/', views.posts),
    path('threads', views.threads, name = 'threads'),
    path('add-thread', views.add_thread, name='add-thread'),
    path('add-post/<int:thread_id>/', views.add_post),
    path('file/<int:file_id>/', views.download_file),

    # public ajax requests
    path('ajax/stats/', views.ajax_get_stats),

    # login restricted requests
    path('ajax/<ajax_request>/', csrf_exempt(views.ajax)),
    path('ajax/<ajax_request>/<int:object_id>/', csrf_exempt(views.ajax)),
]