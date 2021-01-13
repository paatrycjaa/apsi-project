import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone

from . import models
from . import attachment
from . import utils

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
        dt = timezone.localtime(timezone.now())
        thread = models.Watek(temat = data['thema'], data_dodania = dt, data_ostatniego_posta = dt)
        thread.save()
        post = models.Post(tytul=data['thema'], tresc=data['content'], watek=thread, uzytkownik = user, data_dodania=dt)
        post.save()

        message = "Wątek i pierwszy post dodany"
        status = True
    
    except Exception as e:
        status = False
        message = utils.handle_exception(e)
    finally:
        return json.dumps({'status': status})

def add_post(request, user):
    try:
        data = json.loads(request.POST['data'])

        user = models.Uzytkownik.objects.get(user_id=user.id)
        thread = models.Watek.objects.get(id=data['thread'])
        dt = timezone.localtime(timezone.now())
        post = models.Post(tytul=data['thema'], tresc=data['content'], watek=thread, uzytkownik = user, data_dodania=dt)
        post.save()
        models.Watek.objects.filter(id=data['thread']).update(data_ostatniego_posta = dt)

        for file_name, file_size, file in zip(data['attachments'], data['attachments_size'], request.FILES.values()):
            att_key = attachment.add_post_attachment(post, file_name, file_size)
            attachment.save_file(file, file_name, att_key)

        message="Post został dodany"
        status = True

    except Exception as e:
        status = False
        message = utils.handle_exception(e)
    finally:
        return json.dumps({'status': status})

