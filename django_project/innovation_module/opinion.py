import json
import datetime

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Case, When, BooleanField

from . import models
from . import idea
from . import utils


def serialize(objects):
    return json.dumps(list(objects), cls=DjangoJSONEncoder)

def get_opinions(id, user_obj):
    pomysl = models.Pomysl.objects.get(pk=id)
    status = models.StatusPomyslu.objects.get(pk="Oczekujacy")
    return models.Ocena.objects.filter(pomysl=pomysl).annotate(is_editable=Case(
        When(pomysl__status_pomyslu=status, uzytkownik=user_obj, then=True), default=False, output_field=BooleanField()
    )).order_by('data').values()

def get_opinions_json(pomysl, user):
    user_obj = models.Uzytkownik.objects.get(user=user)
    return serialize(get_opinions(pomysl, user_obj))

def get_opinion(opinion_id):
    return models.Ocena.objects.get(pk=opinion_id)

def get_opinion_json(opinion_id):
    return serialize(models.Ocena.objects.filter(pk=opinion_id).values())

def get_add_opinion_json(idea_id):
    settings = idea.get_settings(idea_id)
    data = {
        'opinion_id': '',
        'idea_id': idea_id,
        'settings': settings
    }

    return data

def get_edit_opinion_json(opinion_id):
    opinion = get_opinion(opinion_id)
    settings = idea.get_settings(opinion.pomysl.pk)
    data = {
        'opinion_id': opinion_id,
        'idea_id': opinion.pomysl.pk,
        'settings': settings    }

    return data

def add_opinion(opinion_json, user):
    try:
        data = json.loads(opinion_json)
        idea_id = data['idea_id']

        user = models.Uzytkownik.objects.get(user_id=user.id)

        if not idea.can_opinion_be_added(idea_id, user):
            status = False
            message = "Opinion cannot be added"
            return

        settings = idea.get_settings(idea_id)

        pomysl=models.Pomysl.objects.get(pk=idea_id)

        m = models.Ocena(data=datetime.datetime.now(), pomysl=pomysl, uzytkownik=user)

        if 'num' in settings:
            m.ocena_liczbowa = data['rate']
        if 'text' in settings:
            m.opis=data['description']

        m.save()

        if 'num' in settings:
            idea.update_average_rating(idea_id)

        status = True
        message = "Opinion added"

    except Exception as e:
        status = False
        message = utils.handle_exception(e)
    finally:
        return json.dumps({'status': status, 'message': message})

def edit_opinion(opinion_json):
    try:
        data = json.loads(opinion_json)

        idea_id = data['idea_id']

        settings = idea.get_settings(idea_id)

        m = models.Ocena.objects.get(pk=data['opinion_id'])

        if 'num' in settings:
            m.ocena_liczbowa = data['rate']
        if 'text' in settings:
            m.opis=data['description']

        m.save()

        if 'num' in settings:
            idea.update_average_rating(idea_id)

        status = True
        message = "Opinion changed"

    except Exception as e:
        status = False
        message = utils.handle_exception(e)
    finally:
        return json.dumps({'status': status, 'message': message})

def count_all():
    return models.Ocena.objects.count()

def count_date(date):
    return models.Ocena.objects.filter(
        data__year=date.year,
        data__month=date.month,
        data__day=date.day
        ).count()

def remove_opinion(opinion_id):
    try:
        opinion = models.Ocena.objects.get(pk=opinion_id)
        idea_id = opinion.pomysl.pk
        opinion.delete()

        idea.update_average_rating(idea_id)

        status = True
        message = "Opinion removed"

    except Exception as e:
        status = False
        message = utils.handle_exception(e)
    finally:
        return json.dumps({'status': status, 'message': message})