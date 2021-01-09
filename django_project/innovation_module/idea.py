import json
import datetime

from django.core import serializers

from . import models
from .models import Pomysl

def serialize(objects):
    # raw = serializers.serialize('python', objects)
    # return json.dumps([o['fields'] for o in raw])
    return serializers.serialize('json', objects)

def idea_exists(topic):
    Pomysl.objects.filter(tematyka=topic).count() > 0

def add_idea(idea_json, user):

    try:
        data = json.loads(idea_json)

        if idea_exists(data['topic']):
            message = "Idea already exists"
            status = False
            return

        if data['num_rating'] and data['text_rating']:
            settings_val = 'num_text'
        elif data['num_rating']:
            settings_val = 'num_only'
        elif data['text_rating']:
            settings_val = 'text_only'
        else:
            settings_val = 'brak'
       

        user = models.Uzytkownik.objects.get(user_id=user.id)
        status = models.StatusPomyslu.objects.get(status='Oczekujacy')
        settings = models.UstawieniaOceniania.objects.get(ustawienia=settings_val)

        m = models.Pomysl(tematyka=data['topic'], opis=data['description'], planowane_korzysci=data['benefits'],
                          planowane_koszty=data['costs'], uzytkownik=user, status=status, ustawienia_oceniania=settings,
                          ocena_wazona=-1)
        m.save()

        message = "Idea added"
        status = True

    except Exception as e:
        print('error occured when adding idea')
        if hasattr(e, 'message'):
            print(e.message)
            message = e.message
        else:
            print(e)
            message = e.__str__()
        status = False
    finally:
        return json.dumps({'status': status})

def edit_idea(idea_json):
    try:
        data = json.loads(idea_json)
        print(data)
        idea_id = data['idea_id']

        idea = models.Pomysl.objects.get(pk=idea_id)

        new_status = models.StatusPomyslu.objects.get(status='Zablokowany')

        idea.status = new_status

        idea.save()

        message = "Idea edited"

        status = True

    except Exception as e:
        print('error occured when editing idea')
        if hasattr(e, 'message'):
            print(e.message)
            message = e.message
        else:
            print(e)
            message = e.__str__()
        status = False
    finally:
        return json.dumps({'status': status, 'message': message})

def get_ideas(user = None):
    if user is None:
        return Pomysl.objects.all()
    user = models.Uzytkownik.objects.get(user_id=user.id)
    return Pomysl.objects.filter(uzytkownik=user)

def get_idea(idea_id):
    return Pomysl.objects.filter(
        pk=idea_id
    )

def get_ideas_json(user=None):
    return serialize(get_ideas(user))

def get_idea_json(idea_id):
    return serialize(get_idea(idea_id))

def get_settings(idea_id):
    return Pomysl.objects.get(pk=idea_id).ustawienia_oceniania.ustawienia

def can_opinion_be_added(idea_id):
    status = models.StatusPomyslu.objects.get(status='Oczekujacy')
    return Pomysl.objects.get(pk=idea_id).status == status

def update_average_rating(idea_id, new_rating, old_rating = None):
    """Should be called after new rating is saved to the database.
    """
    idea = Pomysl.objects.get(pk=idea_id)
    ratings_num = models.Ocena.objects.filter(pomysl=idea).count()
    if old_rating is None:
        new_avg = (idea.ocena_wazona * (ratings_num - 1) + int(new_rating)) / ratings_num
    else:
        new_avg = (idea.ocena_wazona * ratings_num + int(new_rating) - int(old_rating)) / ratings_num
    idea.ocena_wazona = new_avg
    idea.save()
