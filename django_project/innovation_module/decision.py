from . import models
from django.core import serializers
import json
import datetime

def serialize(objects):
    # raw = serializers.serialize('python', objects)
    # return json.dumps([o['fields'] for o in raw])
    return serializers.serialize('json', objects)


def get_filtered_ideas_json(stat):
    return serialize(get_filtered_ideas(stat))

def get_filtered_ideas(stat):
    return models.Pomysl.objects.filter(status=stat)

def add_decision(decision_json):

    try:
        data = json.loads(decision_json)

        user = models.Uzytkownik.objects.first()
        pomysl=models.Pomysl.objects.get(pk=data['id'])
        werdykt = models.RodzajDecyzji.objects.get(rodzaj_decyzji=data['werdykt'])
        

        m = models.Decyzja(data=datetime.datetime.now(), uzasadnienie=data['description'], pomysl=pomysl,
                          werdykt=werdykt, uzytkownik=user)
        m.save()
        if(data['werdykt']!="Prosba o uzupelnienie"):
            statusp = models.StatusPomyslu.objects.get(status=data['werdykt'])
        else: 
            statusp = models.StatusPomyslu.objects.get(status="Edycja")
        pom = models.Pomysl.objects.get(id=data['id'])
        pom.status=statusp
        pom.save()
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