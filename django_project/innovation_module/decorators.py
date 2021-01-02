""" Custom decorators. """

from functools import wraps
from django.conf import settings
from django.core.exceptions import PermissionDenied

from . import models


def users_opinion(function):
    """ Decorator for restricting access to not own opinion.
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
