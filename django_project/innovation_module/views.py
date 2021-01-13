from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required, user_passes_test


import json

from . import idea, opinion, decorators, forum, decision, attachment

_ajax_requests = {
    'get_keywords': lambda request, object_id: idea.get_keywords(),
    'all_ideas': lambda request, object_id: idea.get_ideas_json(request.user, False, True),
    'user_ideas': lambda request, object_id: idea.get_ideas_json(request.user, True, False),
    'submit_idea': lambda request, object_id: idea.add_idea(request, request.user),
    'edit_idea': lambda request, object_id: ajax_edit_idea(request, int(json.loads(request.POST['data'])['idea_id'])),
    'get_idea': lambda request, object_id: idea.get_idea_json(object_id),
    'all_opinions': lambda request, object_id: opinion.get_opinions_json(object_id, request.user),
    'get_opinion': lambda request, object_id: opinion.get_opinion_json(object_id),
    'submit_opinion': lambda request, object_id: opinion.add_opinion(request.body.decode('utf-8'), request.user),
    'submit_decision': lambda request, object_id: decision.add_decision(request.body.decode('utf-8'), request.user),
    'edit_opinion': lambda request, object_id: ajax_edit_opinion(request, int(json.loads(request.body)['opinion_id'])),
    'filtered_ideas': lambda request, object_id: idea.get_ideas_json(request.user, False, False),
    'get_thread': lambda request, object_id: forum.get_thread_json(object_id),
    'all_threads': lambda request, object_id: forum.get_threads_json(),
    'all_posts': lambda request, object_id: forum.get_posts_json(object_id),
    'submit_thread': lambda request, object_id: forum.add_thread(request.body.decode('utf-8'), request.user),
    'submit_post': lambda request, object_id: forum.add_post(request, request.user),
    'block_idea':  lambda request, object_id: ajax_block_idea(request, object_id),
    'remove_idea': lambda request, object_id: ajax_remove_idea(request, object_id),
    'remove_thread': lambda request, object_id: ajax_remove_thread(request, object_id)
    'change_status': lambda request, object_id: decision.change_status(request.body.decode('utf-8'),request.user)
}    
    

def home(request):
    return render(request, 'app/static/home.html')

@login_required
def ideas(request):
    return render(request, 'app/components/ideas-list/ideasList.html')
@login_required
def ideasfiltered(request, status_pomyslu):
    context = {
        'status': status_pomyslu
    }
    return render(request,'app/components/ideas-filtered/ideasFiltered.html',context)

@login_required
def my_ideas(request):
    return render(request, 'app/components/my-ideas-list/myIdeasList.html')

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
@decorators.users_idea
def edit_idea(request, idea_id):    
    context = {'idea_id': idea_id}
    return render(request, 'app/components/idea-addition/ideaAddition.html', context)

@login_required
def ajax(request, ajax_request, object_id=None):
    try:
        data = _ajax_requests[ajax_request](request, object_id)
        return HttpResponse(data, content_type='application/json')
    except KeyError:
        print('Key ', ajax_request, ' not found')
        return HttpResponseNotFound('Cannot handle ajax request. Wrong request.')
    except Exception as e:
        print('error occured when editing data')
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        return HttpResponseNotFound('Cannot handle ajax request. Server error.')


@decorators.users_opinion
def ajax_edit_opinion(request, opinion_id):
    body_unicode = request.body.decode('utf-8')
    return opinion.edit_opinion(body_unicode)

@login_required
def download_file(request, file_id):
    return attachment.download_file(file_id)

@decorators.users_idea
def ajax_edit_idea(request, idea_id):
    return idea.edit_idea(request, request.user)

@user_passes_test(lambda u : u.is_superuser)
def ajax_block_idea(request, object_id):
    return idea.block_idea(object_id)

@user_passes_test(lambda u : u.is_superuser)
def ajax_remove_idea(request, object_id):
    return idea.remove_idea(object_id)

@user_passes_test(lambda u : u.is_superuser)
def ajax_remove_thread(request, object_id):
    return forum.remove_thread(object_id)
