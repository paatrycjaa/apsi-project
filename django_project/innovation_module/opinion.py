import json
import datetime

from django.core import serializers

from . import models
from . import idea

def serialize(objects):
    # raw = serializers.serialize('python', objects)
    # return json.dumps([o['fields'] for o in raw])
    return serializers.serialize('json', objects)

def get_opinions(id):
    pomysl = models.Pomysl.objects.filter(pk=id)
    return models.Ocena.objects.filter(
        pomysl=pomysl[0]
    )

def get_opinions_json(pomysl):
    return serialize(get_opinions(pomysl))

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
        
    except Exception as e:
        print('error occured when adding opinion')
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        status = False
    finally:
        return json.dumps({'status': status})

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
        
    except Exception as e:
        print('error occured when adding opinion')
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        status = False
    finally:
        return json.dumps({'status': status})
