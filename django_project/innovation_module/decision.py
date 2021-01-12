from . import models
from django.core import serializers
import json
from django.utils import timezone

def serialize(objects):
    # raw = serializers.serialize('python', objects)
    # return json.dumps([o['fields'] for o in raw])
    return serializers.serialize('json', objects)


def get_filtered_ideas_json(stat):
    return serialize(get_filtered_ideas(stat))

def get_filtered_ideas(stat):
    status = models.StatusPomyslu.objects.get(status=stat)
    return models.Pomysl.objects.all()

def add_decision(decision_json, user):

    try:
        data = json.loads(decision_json)

        board_member = models.CzlonekKomisji.objects.get(decyzja=user.id)  
        pomysl=models.Pomysl.objects.get(pk=data['id'])
        werdykt = models.RodzajDecyzji.objects.get(rodzaj_decyzji=data['werdykt'])

        m = models.Decyzja(data=timezone.localtime(timezone.now()), uzasadnienie=data['description'], pomysl=pomysl,
                          rodzaj_decyzji=werdykt, czlonek_komisji=board_member)
        m.save()

        if(data['werdykt']!="Prosba o uzupelnienie"):
            statusp = models.StatusPomyslu.objects.get(status=data['werdykt'])
        else: 
            statusp = models.StatusPomyslu.objects.get(status="Edycja")

        pom = models.Pomysl.objects.get(id=data['id'])
        pom.status_pomyslu=statusp
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

def change_status(status_update, user):
    try:
        data = json.loads(status_update)
        idea = models.Pomysl.objects.get(pk=data['id'])
        new_status = models.StatusPomyslu.objects.get(status=data['status_update'])

        idea.status_pomyslu = new_status
        idea.save()

        status = True
        message = "Idea blocked"

    except Exception as e:
        print('error occured when blocking idea')
        if hasattr(e, 'message'):
            print(e.message)
            message = e.message
        else:
            print(e)
            message = e.__str__()
        status = False
    finally:
        return json.dumps({'status': status, 'message': message})