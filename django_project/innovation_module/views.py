from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

import json

from . import idea, opinion, decorators

def home(request):
    return render(request, 'app/static/home.html')

@login_required
def ideas(request):
    return render(request, 'app/components/ideas-list/ideasList.html')

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
def add_opinion(request, idea_id):    
    context = opinion.get_add_opinion_json(idea_id)
    return render(request, 'app/components/opinion-addition/opinionAddition.html', context)

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
    if ajax_request == 'edit_idea':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(idea.edit_idea(body_unicode), content_type='application/json')     
    if ajax_request == 'get_idea':
        return HttpResponse(idea.get_idea_json(object_id), content_type='application/json')
    if ajax_request == 'all_opinions':
        return ajax_get_all_opinions(request, object_id)
    if ajax_request == 'get_opinion':
        return HttpResponse(opinion.get_opinion_json(object_id), content_type='application/json')
    if ajax_request == 'submit_opinion':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(opinion.add_opinion(body_unicode, request.user),content_type='application/json')
    if ajax_request == 'edit_opinion':
        return ajax_edit_opinion(request, int(json.loads(request.body)['opinion_id']))
    return HttpResponseNotFound('Cannot handle ajax request')

def ajax_get_all_opinions(request, idea_id):
    return HttpResponse(opinion.get_opinions_json(idea_id, request.user), content_type='application/json')

@decorators.users_opinion
def ajax_edit_opinion(request, opinion_id):
    body_unicode = request.body.decode('utf-8')
    return HttpResponse(opinion.edit_opinion(body_unicode), content_type='application/json')
