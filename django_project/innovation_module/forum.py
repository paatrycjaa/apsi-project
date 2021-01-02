import json
import datetime

from django.core import serializers

from . import models

def serialize(objects):
    return serializers.serialize('json', objects)

def get_threads():
    return models.Watek.objects.all()

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
    return models.Post.objects.filter(watek = watek[0])

def get_posts_json(watek_id):
    return serialize(get_posts(watek_id))