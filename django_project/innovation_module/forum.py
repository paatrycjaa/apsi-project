import json
import datetime

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone

from . import models
from . import attachment

def serialize(objects):
    return serializers.serialize('json', objects)

def get_threads():
    return models.Watek.objects.all().order_by('data_dodania')

def get_threads_json():
    return serialize(get_threads())

def get_thread(id):
    return models.Watek.objects.filter(
        pk=id
    )

def get_thread_json(id):
    return serialize(get_thread(id))

def get_posts(id):
    watek=models.Watek.objects.filter(pk=id)
    return models.Post.objects.filter(watek = watek[0]).order_by('data_dodania')

def get_posts_json(watek_id):
    posts = get_posts(watek_id)
    posts_values = posts.values()

    for p, obj in zip(posts_values, posts):
        p['attachments'] = list(models.ZalacznikPosta.objects.filter(post=obj).values('pk', 'zalacznik__nazwa_pliku', 'zalacznik__rozmar'))

    return json.dumps(list(posts_values), cls=DjangoJSONEncoder)
    
def thread_exist(thema):
    models.Watek.objects.filter(temat=thema).count() > 0

def add_thread(thread_json, user):

    try:
        data = json.loads(thread_json)

        if thread_exist(data['thema']):
            message = "Taki wątek już istnieje"
            status = False
            return
        
        user = models.Uzytkownik.objects.get(user_id=user.id)
        dt = datetime.datetime.now()
        thread = models.Watek(temat = data['thema'], data_dodania = dt, data_ostatniego_posta = dt)
        thread.save()
        post = models.Post(tytul=data['thema'], tresc=data['content'], watek=thread, uzytkownik = user, data_dodania=dt)
        post.save()

        message = "Wątek i pierwszy post dodany"
        status = True
    
    except Exception as e:
        print('Wystąpił bład podczas dodawania wątku')
        if hasattr(e, 'message'):
            print(e.message)
            message = e.message
        else:
            print(e)
            message = e.__str__()
        status = False
    finally:
        return json.dumps({'status': status})
    
def remove_thread(thread_id):
    try:
        thread = models.Watek.objects.get(pk=thread_id)
        thread.delete()

        status = True
        message = "Thread removed"

    except Exception as e:
        print('error occured when removing thread')
        if hasattr(e, 'message'):
            print(e.message)
            message = e.message
        else:
            print(e)
            message = e.__str__()
        status = False
    finally:
        return json.dumps({'status': status, 'message': message})

def add_post(request, user):
    try:
        data = json.loads(request.POST['data'])

        user = models.Uzytkownik.objects.get(user_id=user.id)
        thread = models.Watek.objects.get(id=data['thread'])
        dt = datetime.datetime.now()
        post = models.Post(tytul=data['thema'], tresc=data['content'], watek=thread, uzytkownik = user, data_dodania=dt)
        post.save()
        models.Watek.objects.filter(id=data['thread']).update(data_ostatniego_posta = dt)

        att_key = attachment.add_post_attachment(post, data['attachment'], data['attachment_size'])
        attachment.save_file(request.FILES['file'], data['attachment'], att_key)

        message="Post został dodany"
        status = True

    except Exception as e:
        print('Wystąpił bład podczas dodawania postu')
        if hasattr(e, 'message'):
            print(e.message)
            message = e.message
        else:
            print(e)
            message = e.__str__()
        status = False

    finally:
        return json.dumps({'status': status})

