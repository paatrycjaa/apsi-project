from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required


import json

from . import idea, opinion, decorators, forum, decision

def home(request):
    return render(request, 'app/static/home.html')

@login_required
def ideas(request):
    return render(request, 'app/components/ideas-list/ideasList.html')
@login_required
def ideasfiltered(request):
    return render(request,'app/components/ideas-filtered/ideasFiltered.html')

@login_required
def add_idea(request):
    return render(request, 'app/components/idea-addition/ideaAddition.html')

@login_required
def opinions(request, idea_id):
    context = {
        'idea_id': idea_id
    }
    return render(request, 'app/components/opinions-list/opinionsList.html', context)

@login_required
def posts(request, thread_id):
    context = {
        'thread_id' : thread_id
    }
    return render(request, 'app/components/forum-posts/forumPosts.html', context)

@login_required
def threads(request):
    return render(request, 'app/components/forum-threads/forumThreads.html')

@login_required
def add_post(request, thread_id):
    context = {
        'thread_id' : thread_id
    }
    return render(request, 'app/components/add-posts/addPosts.html', context)

@login_required
def add_thread(request):
    return render(request, 'app/components/add-threads/addThreads.html')

@login_required
def add_opinion(request, idea_id):    
    context = opinion.get_add_opinion_json(idea_id)
    return render(request, 'app/components/opinion-addition/opinionAddition.html', context)
@login_required
def add_decision(request, idea_id):
    context = {
        'idea_id': idea_id,
    }
    return render(request, 'app/components/decision-addition/decisionAddition.html', context)

@login_required
@decorators.users_opinion
def edit_opinion(request, opinion_id):    
    context = opinion.get_edit_opinion_json(opinion_id)
    return render(request, 'app/components/opinion-addition/opinionAddition.html', context)

@login_required
def ajax(request, ajax_request, object_id=None):
    if ajax_request == 'all_ideas':        
        return HttpResponse(idea.get_ideas_json(), content_type='application/json')
    if ajax_request == 'submit_idea':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(idea.add_idea(body_unicode, request.user),content_type='application/json')        
    if ajax_request == 'get_idea':
        return HttpResponse(idea.get_idea_json(object_id), content_type='application/json')
    if ajax_request == 'all_opinions':
        return ajax_get_all_opinions(request, object_id)
    if ajax_request == 'get_opinion':
        return HttpResponse(opinion.get_opinion_json(object_id), content_type='application/json')
    if ajax_request == 'submit_opinion':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(opinion.add_opinion(body_unicode, request.user),content_type='application/json')
    if ajax_request == 'submit_decision':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(decision.add_decision(body_unicode, request.user),content_type='application/json')
    if ajax_request == 'edit_opinion':
        return ajax_edit_opinion(request, int(json.loads(request.body)['opinion_id']))
    if ajax_request == 'filtered_ideas':
        return HttpResponse(decision.get_filtered_ideas_json('Oczekujący'), content_type='application/json')
    if ajax_request == 'all_threads' :
        return HttpResponse(forum.get_threads_json(), content_type='application/json')
    if ajax_request == 'get_thread' :
        return HttpResponse(forum.get_thread_json(object_id), content_type='application/json')
    if ajax_request == 'all_posts' :
        return HttpResponse(forum.get_posts_json(object_id), content_type='application/json')
    if ajax_request == 'submit_thread' :
        body_unicode = request.body.decode('utf-8')
        print(body_unicode)
        return HttpResponse(forum.add_thread(body_unicode, request.user),content_type='application/json')
    if ajax_request == 'submit_post' :
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(forum.add_post(body_unicode, request.user),content_type='application/json')
    return HttpResponseNotFound('Cannot handle ajax request')

def ajax_get_all_opinions(request, idea_id):
    return HttpResponse(opinion.get_opinions_json(idea_id, request.user), content_type='application/json')

@decorators.users_opinion
def ajax_edit_opinion(request, opinion_id):
    body_unicode = request.body.decode('utf-8')
    return HttpResponse(opinion.edit_opinion(body_unicode), content_type='application/json')
