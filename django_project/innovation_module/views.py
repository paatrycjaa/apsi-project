from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from . import idea
from . import opinion
from . import forum

def home(request):
    return render(request, 'app/static/home.html')

def ideas(request):
    return render(request, 'app/components/ideas-list/ideasList.html')

def add_idea(request):
    return render(request, 'app/components/idea-addition/ideaAddition.html')

def opinions(request, idea_id):
    context = {
        'idea_id': idea_id
    }
    return render(request, 'app/components/opinions-list/opinionsList.html', context)

def posts(request, thread_id):
    context = {
        'thread_id' : thread_id
    }
    return render(request, 'app/components/forum-posts/forumPosts.html', context)

def add_opinion(request, idea_id):
    # TODO 
    # move and use external method
    settings = models.Pomysl.objects.get(pk=idea_id).ustawienia_oceniania
    context = {
        'idea_id': idea_id,
        'settings': settings
    }
    return render(request, 'app/components/opinion-addition/opinionAddition.html', context)

def threads(request):
    return render(request, 'app/components/forum-threads/forumThreads.html')

def add_post(request, thread_id):
    return render(request, 'app/components/add-posts/addPosts.html')

def add_thread(request):
    return render(request, 'app/components/add-threads/addThreads.html')

def ajax(request, ajax_request, idea_id=None):
    if ajax_request == 'all_ideas':        
        return HttpResponse(idea.get_ideas_json(), content_type='application/json')
    if ajax_request == 'submit_idea':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(idea.add_idea(body_unicode, request.user),content_type='application/json')
    if ajax_request == 'get_idea':
        return HttpResponse(idea.get_idea_json(idea_id), content_type='application/json')
    if ajax_request == 'all_opinions':
        return HttpResponse(opinion.get_opinions_json(idea_id), content_type='application/json')
    if ajax_request == 'submit_opinion':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(opinion.add_opinion(body_unicode, request.user),content_type='application/json')
    if ajax_request == 'all_threads' :
        return HttpResponse(forum.get_threads_json(), content_type='application/json')
    if ajax_request == 'get_thread' :
        return HttpResponse(forum.get_thread_json(idea_id), content_type='application/json')
    if ajax_request == 'all_posts' :
        return HttpResponse(forum.get_posts_json(idea_id), content_type='application/json')

    return HttpResponseNotFound('Cannot handle ajax request')

