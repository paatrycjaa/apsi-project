from . import models
from django.core import serializers
import json
import datetime

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

def get_filtered_ideas_json(stat):
    return serialize(get_filtered_ideas(stat))

def get_filtered_ideas(stat):
    return models.Pomysl.objects.filter(status=stat)

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



def add_opinion(opinion_json):

    data = json.loads(opinion_json)
    user = models.Uzytkownik.objects.first()


    try:
        data = json.loads(opinion_json)

        user = models.Uzytkownik.objects.first()
        # status = models.StatusPomyslu.objects.get(status='Oczekujacy')
        # settings = models.UstawieniaOceniania.objects.get(ustawienia=settings_val)
        pomysl=models.Pomysl.objects.get(pk=data['id'])

        m = models.Ocena(data=datetime.datetime.now(), ocena_liczbowa=data['rate'], opis=data['description'],pomysl=pomysl, uzytkownik=user)
        m.save()

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


def add_decision(decision_json):

    try:
        data = json.loads(decision_json)

        # user = models.Uzytkownik.objects.first()
        # # status = models.StatusPomyslu.objects.get(status='Oczekujacy')
        # # settings = models.UstawieniaOceniania.objects.get(ustawienia=settings_val)
        # pomysl=models.Pomysl.objects.get(pk=data['id'])

        # m = models.Decyzja(data=datetime.datetime.now(), uzasadnienie=data['description'], pomysl=pomysl,
        #                   werdykt=data['werdykt'], uzytkownik=user)
        # m.save()

        status = True
        

    except Exception as e:
        print('error occured when adding decision')
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        status = False
    finally:
        return json.dumps({'status': status})



