""" Custom decorators. """

from functools import wraps
from django.conf import settings
from django.core.exceptions import PermissionDenied

from . import models


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
    """ Decorator for restricting edit acces to not user's idea
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