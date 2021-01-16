import json
import datetime

from django.core import serializers

from . import models
from . import idea
from . import utils

def serialize(objects):
    return serializers.serialize('json', objects)

def get_opinions(id):
    pomysl = models.Pomysl.objects.filter(pk=id)
    return models.Ocena.objects.filter(
        pomysl=pomysl[0]
    ).order_by('data')

def get_opinions_json(pomysl, user):
    user_obj = models.Uzytkownik.objects.get(user=user)
    opinions = json.loads(serialize(get_opinions(pomysl)))
    for op in opinions:
        is_editable = False
        if (op['fields']['uzytkownik'] == user_obj.pk):
            is_editable= True
        op['isEditable'] = is_editable
    return json.dumps(opinions)

def get_opinion(opinion_id):
    return models.Ocena.objects.get(pk=opinion_id)

def get_opinion_json(opinion_id):
    return serialize(models.Ocena.objects.filter(pk=opinion_id))

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

        if not idea.can_opinion_be_added(idea_id):
            status = False
            return

        settings = idea.get_settings(idea_id)

        user = models.Uzytkownik.objects.get(user_id=user.id)
        pomysl=models.Pomysl.objects.get(pk=idea_id)

        m = models.Ocena(data=datetime.datetime.now(), pomysl=pomysl, uzytkownik=user)

        if 'num' in settings:
            m.ocena_liczbowa = data['rate']
        if 'text' in settings:
            m.opis=data['description']

        m.save()

        if 'num' in settings:
            idea.update_average_rating(idea_id, data['rate'])

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

        old_rate = m.ocena_liczbowa

        if 'num' in settings:
            m.ocena_liczbowa = data['rate']
        if 'text' in settings:
            m.opis=data['description']

        m.save()

        if 'num' in settings:
            idea.update_average_rating(idea_id, data['rate'], old_rate)

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
