from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ideas', views.ideas, name='ideas'),
    path('add-idea', views.add_idea, name='add_idea'),
]
