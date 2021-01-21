""" Custom decorators. """

from functools import wraps
from django.conf import settings
from django.core.exceptions import PermissionDenied

from . import models, user

def login_required_permission_denied(function):
    """ Restricting ajax requests with permission denied error (no redirecting)
    """
    @wraps(function)
    def wrap(request, ajax_request, object_id=None, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, ajax_request, object_id, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def user_is_jury(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if user.is_user_jury(request.user):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def users_opinion(function):
    """ Decorator for restricting edit access to not user's opinion
    """
    @wraps(function)
    def wrap(request, opinion_id, *args, **kwargs):
        opinion = models.Ocena.objects.get(pk=opinion_id)
        uzytkownik = models.Uzytkownik.objects.get(user=request.user)
        if uzytkownik == opinion.uzytkownik:
            return function(request, opinion_id, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap

def users_idea(function):
    """ Decorator for restricting edit access to not user's idea
    """
    @wraps(function)
    def wrap(request, idea_id, *args, **kwargs):
        idea = models.Pomysl.objects.get(pk=idea_id)
        uzytkownik = models.Uzytkownik.objects.get(user=request.user)
        if uzytkownik == idea.uzytkownik:
            return function(request, idea_id, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap