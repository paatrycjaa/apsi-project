from . import models
from django.core import serializers
import json

def serialize(objects):
    # raw = serializers.serialize('python', objects)
    # return json.dumps([o['fields'] for o in raw])
    return serializers.serialize('json', objects)

def get_ideas(user = None):
    if user is None:
        return models.Pomysl.objects.all()
    
    return models.Pomysl.objects.get(user=user)

def get_idea(id):
    return models.Pomysl.objects.filter(
        pk=id
    )

def get_ideas_json(user=None):
    return serialize(get_ideas(user))

def get_idea_json(id):
    return serialize(get_idea(id))

def get_opinions(id):
    pomysl = models.Pomysl.objects.filter(pk=id)
    return models.Ocena.objects.filter(
        pomysl=pomysl[0]
    )

def get_opinions_json(pomysl):
    return serialize(get_opinions(pomysl))


def add_idea(idea_json):

    try:
        data = json.loads(idea_json)

        if data['num_rating'] and data['text_rating']:
            settings_val = 'num_text'
        elif data['num_rating']:
            settings_val = 'num_only'
        elif data['text_rating']:
            settings_val = 'text_only'
        else:
            settings_val = 'brak'

        user = models.Uzytkownik.objects.first()
        status = models.StatusPomyslu.objects.get(status='Oczekujacy')
        settings = models.UstawieniaOceniania.objects.get(ustawienia=settings_val)

        m = models.Pomysl(tematyka=data['topic'], opis=data['description'], planowane_korzysci=data['benefits'],
                          planowane_koszty=data['costs'], uzytkownik=user, status=status, ustawienia_oceniania=settings,
                          ocena_wazona=-1)
        m.save()

        status = True

    except Exception as e:
        print('error occured when adding idea')
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        status = False
    finally:
        return json.dumps({'status': status})
