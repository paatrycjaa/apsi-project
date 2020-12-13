from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from . import db_view

def home(request):
    return render(request, 'app/static/home.html')

def ideas(request):
    return render(request, 'app/components/ideas-list/ideasList.html')

def add_idea(request):
    return render(request, 'app/components/idea-addition/ideaAddition.html')

def opinions(request):
    return render(request, 'app/components/opinions-list/opinionsList.html')

# def add_opinion(request):
#     return render(request, 'app/components/idea-addition/ideaAddition.html')

def ajax(request, ajax_request):
    if ajax_request == 'all_ideas':        
        return HttpResponse(db_view.get_ideas_json(), content_type='application/json')
    if ajax_request == 'submit_idea':
        body_unicode = request.body.decode('utf-8')
        return HttpResponse(db_view.add_idea(body_unicode),content_type='application/json')
    if ajax_request == 'all_opinions':
        return HttpResponse(db_view.get_opinions_json(), content_type='application/json')
    return HttpResponseNotFound('Cannot handle ajax request')
