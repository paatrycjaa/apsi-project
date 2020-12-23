from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from . import idea
from . import opinion

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

def add_opinion(request, idea_id):    
    settings = idea.get_settings(idea_id)
    context = {
        'idea_id': idea_id,
        'settings': settings
    }
    return render(request, 'app/components/opinion-addition/opinionAddition.html', context)

def ajax(request, ajax_request, idea_id=None):
    if ajax_request == 'all_ideas':        
        return HttpResponse(idea.get_ideas_json(), content_type='application/json')
    if ajax_request == 'submit_idea':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(idea.add_idea(body_unicode),content_type='application/json')
    if ajax_request == 'get_idea':
        return HttpResponse(idea.get_idea_json(idea_id), content_type='application/json')
    if ajax_request == 'all_opinions':
        return HttpResponse(opinion.get_opinions_json(idea_id), content_type='application/json')
    if ajax_request == 'submit_opinion':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(opinion.add_opinion(body_unicode),content_type='application/json')
    return HttpResponseNotFound('Cannot handle ajax request')

