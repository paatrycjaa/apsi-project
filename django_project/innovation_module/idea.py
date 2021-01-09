import json
import datetime

from django.core import serializers
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone

from . import models
from .models import Pomysl

def serialize(objects, user, filter_status):

    if filter_status:
        objects = [x for x in objects if x['status_pomyslu_id'] == 'Oczekujacy']
    
    for elem in objects:        
        isCurrentUser = elem['uzytkownik_id'] == user
        elem['is_current_user'] = isCurrentUser
        elem.pop('uzytkownik_id')

    return json.dumps(list(objects), cls=DjangoJSONEncoder)

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
        keyword = models.SlowoKluczowe.objects.get(slowo_kluczowe=data['category'])

        m = models.Pomysl(tematyka=data['topic'], opis=data['description'], planowane_korzysci=data['benefits'], slowo_kluczowe=keyword,
                          planowane_koszty=data['costs'], uzytkownik=user, status_pomyslu=status, ustawienia_oceniania=settings,
                          ocena_wazona=-1, data_dodania=timezone.localtime(timezone.now()))
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

        idea.status_pomyslu = new_status
        idea.data_ostatniej_edycji = timezone.localtime(timezone.now())

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

def get_ideas(user, filter_user):
    
    objs = Pomysl.objects
    
    if filter_user:
        user_obj = models.Uzytkownik.objects.get(user_id=user.id)
        objs = objs.filter(uzytkownik=user_obj)

    return objs.annotate(attachment_count=Count('zalacznikpomyslu')).values()        

def get_ideas_json(user, filter_user):
    filter_status = not filter_user
    return serialize(get_ideas(user, filter_user), user, filter_status)

def get_idea_json(idea_id):
    ideas = Pomysl.objects.filter(pk=idea_id)
    if len(ideas) == 0:
        raise ValueError('idea_id: {} is not valid.'.format(idea_id))
    
    idea_dict = ideas.values()[0]

    idea_dict['attachments'] = list(models.ZalacznikPomyslu.objects.filter(pomysl=ideas[0]).values('pk', 'zalacznik__nazwa_pliku'))

    return json.dumps(idea_dict, cls=DjangoJSONEncoder)

def get_settings(idea_id):
    return Pomysl.objects.get(pk=idea_id).ustawienia_oceniania.ustawienia

def can_opinion_be_added(idea_id):
    status = models.StatusPomyslu.objects.get(status='Oczekujacy')
    return Pomysl.objects.get(pk=idea_id).status_pomyslu == status

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


def edit_idea(idea_json, user):
    try:
        data = json.loads(idea_json)

        if idea_exists(data['topic']):
            message = "Idea already exists"
            status = False
            return
        
        m = models.Pomysl.objects.get(pk=data['idea_id'])

        m.tematyka=data['topic']
        m.opis=data['description']
        m.planowane_korzysci=data['benefits']
        m.planowane_koszty=data['costs']
               
        if data['num_rating'] and data['text_rating']:
            settings_val = 'num_text'
        elif data['num_rating']:
            settings_val = 'num_only'
        elif data['text_rating']:
            settings_val = 'text_only'
        else:
            settings_val = 'brak'


        m.uzytkownik = models.Uzytkownik.objects.get(user_id=user.id)
        m.status_pomyslu = models.StatusPomyslu.objects.get(status='Oczekujacy')
        m.ustawienia_oceniania = models.UstawieniaOceniania.objects.get(ustawienia=settings_val)


        m.save()

        message = "Idea added"
        status = True

    
    except Exception as e:
        print('error occured when editing data')
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        status = False
    finally:
        return json.dumps({'status': status})

 
def get_keywords():
    keywords = models.SlowoKluczowe.objects.values_list('slowo_kluczowe', flat=True)
    return json.dumps(list(keywords), cls=DjangoJSONEncoder)