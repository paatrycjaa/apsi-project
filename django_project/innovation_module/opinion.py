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


def add_opinion(opinion_json):
    try:
        data = json.loads(opinion_json)
        idea_id = data['id']

        if not idea.can_opinion_be_added(idea_id):
            status = False
            return

        settings = idea.get_settings(idea_id)

        user = models.Uzytkownik.objects.first()
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

